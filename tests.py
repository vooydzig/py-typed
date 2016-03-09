from unittest import TestCase

from typed import accepts, returns


class AcceptsTestCase(TestCase):
    def test_accepts_does_not_modify_return_value(self):
        @accepts()
        def foo():
            return 1

        self.assertEqual(foo(), 1)

    def test_accepts_raises_ValueError_when_argument_count_mismatches(self):
        @accepts()
        def foo(a):
            return a

        self.assertRaises(ValueError, foo, 1)

    def test_accepts_raises_TypeError_when_type_mismatches(self):
        @accepts(a=int)
        def foo(a):
            return a

        self.assertRaises(TypeError, foo, 'a')

    def test_accepts_raises_TypeError_when_type_mismatches_for_named_args(self):
        @accepts(a=int)
        def foo(a):
            return a

        self.assertRaises(TypeError, foo, a='test')

    def test_accepts_raises_TypeError_when_type_is_not_subclass_of_declared_type(self):
        class Foo(object):
            pass

        class Bar(object):
            pass

        @accepts(a=Foo)
        def foo(a):
            return a

        self.assertRaises(TypeError, foo, Bar())


class ReturnsTestCase(TestCase):
    def test_returns_raises_TypeError_when_return_value_mismatches_declared_type(self):
        @returns(int)
        def foo():
            return 'test'

        self.assertRaises(TypeError, foo)

    def test_returns_raises_TypeError_when_return_value_is_not_subclass_of_declared_type(self):
        class Foo(object):
            pass

        class Bar(object):
            pass

        @returns(Foo)
        def foo():
            return Bar()

        self.assertRaises(TypeError, foo)
