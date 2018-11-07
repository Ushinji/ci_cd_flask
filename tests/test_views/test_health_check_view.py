from tests import Base


class TestHealthCheckView(Base):

    def setUp(self):
        super().setUp()

    def test_200を返すこと(self):
        response = self.api_get('/health_check')
        self.assertEqual(response.status_code, 200)
