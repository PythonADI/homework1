import contextlib
import io
from pathlib import Path
from unittest import TestCase
from homework1.main import main


class TestMainFunction(TestCase):
    def test_main(self):
        base_dir = Path(__file__).resolve().parent.parent
        read_me = base_dir / 'README.md'
        with io.StringIO() as buf:
            with contextlib.redirect_stdout(buf):
                main()

            exercises = [
                exercise[3:]
                for exercise in
                read_me.read_text().split('\n')[6:]
            ]
            output = buf.getvalue().split('\n')[:-1]
            for i, (done_exercise, exercise) in enumerate(zip(output, exercises[:-1]), start=1):
                msg = f'Wrong answer for exercise {i}: {exercise}, you have {done_exercise}'
                self.assertEqual(
                    done_exercise,
                    str(eval(exercise)),
                    msg
                )
