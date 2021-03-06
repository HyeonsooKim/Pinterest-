from django.contrib.auth.forms import UserCreationForm

class AccountUpdateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        #username 비활성화 -> 잘못보낸다 하더라도 반영되지 않음
        self.fields['username'].disabled = True