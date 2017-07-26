from config import ApplicationConfig
import unittest

class TestApplicationConfig(unittest.TestCase):
    def tearDown(self):
        ApplicationConfig.reset_instance()

    def test_incorrect_environment_error(self):
        expected_error_msg = "environment has to be one of {}".format(ApplicationConfig.ALLOWED_ENVS)

        with self.assertRaises(ValueError) as config:
            ApplicationConfig("foo")

        self.assertEqual(expected_error_msg, str(config.exception))

    def test_sets_environment(self):
        environment = "production"
        config = ApplicationConfig(environment)

        self.assertEqual(config.environment, environment)

    def test_get_instance_does_not_override_anything(self):
        environment = "production"
        config = ApplicationConfig.get_instance(environment)
        config2 = ApplicationConfig.get_instance()

        self.assertEqual(id(config), id(config2))
        self.assertEqual(environment, config2.environment)

    def test_debug_mode_is_enabled_in_development_environment(self):
        config = ApplicationConfig("development")

        self.assertTrue(config.debug_mode_is_enabled())

    def test_debug_mode_is_enabled_in_production_environment(self):
        config = ApplicationConfig("production")

        self.assertFalse(config.debug_mode_is_enabled())
