import contextlib
import io
from pathlib import Path
from unittest import TestCase
from homework1.main import main


class TestMainFunction(TestCase):
    def test_main(self):
        base_dir = Path(__file__).resolve().parent.parent
        with io.StringIO() as buf:
            with contextlib.redirect_stdout(buf):
                main()

            exercises = [
                'Hello World!',
                5 + 7,
                37 - 8,
                -90 * 4,
                100 / 3,
                0.2 + 0.1,
                7.068 * 4.3,
                8 ** 2,
                9 ** 3,
                5 / 3,
                5 // 3,
                99 % 7
            ]

            output = buf.getvalue().split('\n')[:-1]
            self.assertEqual(len(output), len(exercises), msg='Number of exercises does not match')

            for i, (done_exercise, exercise) in enumerate(zip(output, exercises), start=1):
                msg = f'Wrong answer for exercise {i}: {exercise}, you have {done_exercise}'
                self.assertEqual(
                    done_exercise,
                    str(exercise),
                    msg
                )
