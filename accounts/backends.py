from django.contrib.auth.models import User


class EmailBackend(object):

    def authenticate(self, request, username=None, password=None):
        
        try:
          
            user = User.objects.get(email=username)
            
        except User.MultipleObjectsReturned:
            
            user = User.objects.filter(email=username).order_by('id').first()
            print(user)

        except User.DoesNotExist:
            
            return None

        return user
        

    def get_user(self,user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
