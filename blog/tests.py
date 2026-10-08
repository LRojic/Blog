from django.test import TestCase
from django.urls import reverse


class ThemePreferenceTests(TestCase):
    def test_theme_preference_is_shared_by_portfolio_and_blog(self):
        response = self.client.post(
            reverse("set_theme"),
            {"theme": "dark", "next": reverse("post_list")},
        )

        self.assertRedirects(response, reverse("post_list"))
        self.assertContains(self.client.get(reverse("portfolio")), '<body class="dark-mode">')
        self.assertContains(self.client.get(reverse("post_list")), '<body class="dark-mode">')

    def test_theme_can_be_changed_back_to_light(self):
        self.client.post(reverse("set_theme"), {"theme": "dark", "next": "/"})
        self.client.post(reverse("set_theme"), {"theme": "light", "next": "/"})

        self.assertContains(self.client.get(reverse("portfolio")), '<body class="">')

    def test_invalid_theme_is_rejected(self):
        response = self.client.post(
            reverse("set_theme"),
            {"theme": "sepia", "next": "/"},
        )

        self.assertEqual(response.status_code, 400)

    def test_external_redirect_is_not_allowed(self):
        response = self.client.post(
            reverse("set_theme"),
            {"theme": "dark", "next": "https://example.com/"},
        )

        self.assertRedirects(response, reverse("portfolio"))
