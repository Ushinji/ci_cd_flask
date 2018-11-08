from tests import Base
from app.forms.user import UserCreateForm


class TestUserCreateForm(Base):

    def test_Nameの指定がない場合エラーを返す(self):
        self.assertEqual(True, False)

    def test_Emailの指定がない場合エラーを返す(self):
        self.assertEqual(True, False)
