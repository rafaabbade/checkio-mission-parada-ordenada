"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [5, [1500, 1600, 1700, 1700, 1800]],
            "answer": 'S'
        },
        {
            "input": [5, [1900, 1850, 1800, 1750, 1700]],
            "answer": 'N'
        },
        {
            "input": [5, [1600, 1600, 1600, 1600, 1600]],
            "answer": 'S'
        }
    ]
}
