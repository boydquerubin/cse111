import pytest
from workouts import generate_workout, generate_biceps_and_triceps

def test_generate_workout_basic():
    sample_data = [
        ("Chest", "Push-up"),
        ("Legs", "Squat"),
        ("Back", "Pull-up"),
        ("Shoulders", "Press")
    ]
    result = generate_workout(sample_data, 2)
    assert len(result) == 2
    assert all(item in sample_data for item in result)

def test_generate_workout_not_enough_items():
    sample_data = [("Arms", "Curl")]
    result = generate_workout(sample_data, 5)
    assert len(result) == 1
    assert result[0] == ("Arms", "Curl")

def test_generate_biceps_and_triceps_limit():
    biceps = ["Barbell Curl", "Hammer Curl", "Incline Curl", "Cable Curl"]
    triceps = ["Pushdown", "Skullcrusher", "Overhead Extension"]

    selected_biceps, selected_triceps = generate_biceps_and_triceps(biceps, triceps)

    assert len(selected_biceps) <= 3
    assert len(selected_triceps) <= 3
    assert all(b in biceps for b in selected_biceps)
    assert all(t in triceps for t in selected_triceps)

if __name__ == "__main__":
    pytest.main(["-v", "--tb=line", "-rN", __file__])
