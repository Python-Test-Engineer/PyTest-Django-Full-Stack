from django.test import SimpleTestCase, Client, override_settings

# We cannot use RequestFactory as RF does not use middleware


class MaintenanceModeMiddlewareTest(SimpleTestCase):

    def setUp(self):
        self.client = Client()

    @override_settings(MAINTENANCE_MODE=True)
    def test_MSC_501_response_when_maintenance_mode_is_on_simple_test_case(self):
        response = self.client.get("/")
        print(response)
        self.assertContains(response, "maintenance mode")
        self.assertTemplateUsed(response, "maintenance_mode_on.html")

    @override_settings(MAINTENANCE_MODE=False)
    def test_MSC_502_response_when_maintenance_mode_is_off_simple_test_case(self):
        response = self.client.get("/")
        print(response)
        self.assertTemplateNotUsed(response, "maintenance_mode_on.html")


#
