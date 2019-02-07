from datetime import datetime
''' UserCollection class lists, creates, updates
and finds the user information '''

class UsersCollection(object):

    """ place holder for the parent class """
    __user = None

    def __init__(self,client):
        self.client = client

    def __page(self,count, start_index, sort_by):
        response = self.client.get('users?count={}&start_index={}&sort_by=-{}'.format(count,start_index,sort_by))[0]
        return response

    ''' Lists all the users 
        Returns list of user object with default count = 5 users per page '''
    def list(self, sort_by = None):
        count = 5
        start_index = 0
        list_of_users =[]
        user_list = self.client.get('users')[0]
        is_more = user_list['is_more']
        if is_more:
            while is_more and start_index < 20:
                if sort_by:
                    response = self.__page(count, start_index, sort_by=sort_by)
                else:
                    response = self.__page(count, start_index, sort_by='lastModifiedTime')
                is_more = response['is_more']
                start_index = start_index + count
                list_of_users.append(UserResource(response['data'][0]))
            return list_of_users
        return UserResource(user_list['data'])

    ''' Create the user with the specified data
        Returns the UserResource object which has created user information'''
    def create(self, data):
        response = self.client.post('users', data)[0]
        print("CREATE RESPONSE", response)
        return UserResource(response)

    ''' Finds the user information for the requested token 
        Returns the UserResource object which has user information'''
    def find(self,token):
        response = self.client.get('users/{}'.format(token))[0]

        def ssn(self):
            return self.client.get('users/{}/ssn'.format(token))[0]

        return UserResource(response)

    ''' Update the user information for the requested token  with the data
            Returns the UserResource object which has updated user information'''
    def save(self,token , data):
        response = self.client.put('users/{}'.format(token),data)[0]
        return UserResource(response)


''' UserResource class lists all the user properties for the /user endpoint'''

class UserResource(object):

    def __init__(self, user_object):
        self.response = user_object

    @property
    def first_name(self):
        return self.response['first_name']

    @property
    def last_name(self):
        return self.response['last_name']

    @property
    def token(self):
        return self.response['token']

    @property
    def active(self):
        return self.response['active']

    @property
    def gender(self):
        return self.response['gender']

    @property
    def email(self):
        return self.response['email']

    @property
    def phone(self):
        return self.response['phone']

    @property
    def address(self):
        return Address(self.response)

    @property
    def uses_parent_account(self):
        return self.response['uses_parent_account']

    @property
    def corporate_card_holder(self):
        return self.response['corporate_card_holder']

    @property
    def created_time(self):
        return datetime.strptime(self.response['created_time'],'%Y-%m-%dT%H:%M:%SZ')

    @property
    def last_modified_time(self):
        return datetime.strptime(self.response['last_modified_time'],'%Y-%m-%dT%H:%M:%SZ')

    @property
    def metadata(self):
        return self.response['metadata']

    @property
    def birth_date(self):
        print(type(self.response['birth_date']))
        return datetime.strptime(self.response['birth_date'], '%Y-%m-%d').date()

    @property
    def account_holder_group_token(self):
        return self.response['account_holder_group_token']

    @property
    def status(self):
        return self.response['status']

    @property
    def id_card_expiration_date(self):
        return datetime.strptime(self.response['id_card_expiration_date'],'%Y-%m-%d').date()

    @property
    def notes(self):
        return self.response['notes']

    @property
    def ip_address(self):
        return self.response['password']

    @property
    def company(self):
        return self.response['company']

    @property
    def honorific(self):
        return self.response['honorific']

    @property
    def middle_name(self):
        return self.response['middle_name']

    @property
    def nationality(self):
        return self.response['nationality']

    @property
    def passport_number(self):
        return self.response['passport_number']

    @property
    def passport_expiration_date(self):
        return datetime.strptime(self.response['passport_expiration_date'],'%Y-%m-%d').date()

    @property
    def id_card_number(self):
        return self.response['id_card_number']

    @property
    def parent_token(self):
        return self.response['parent_token']

    @property
    def authentication(self):

        return Authentication(self.response['auth_details'])

    @property
    def ssn(self):
        id_details = self.response['ssn']
        return id_details

    @property
    def deposit_account(self):

        account_info = self.response['deposit_account']
        return DepositAccount(account_info)


class Address(object):

    def __init__(self, response):
        self.address1 = response['address1']
        self.address2 = response['address2']
        self.state = response['state']
        self.city = response['city']
        self.country = response['country']
        self.postal_code = response['postal_code']


class DepositAccount(object):

    def __init__(self, account_details):
        self.account_number = account_details['account_number']
        self.routing_number = account_details['routing_number']
        self.allow_immediate_credit = account_details['allow_immediate_credit']
        self.token = account_details['token']
        self.user_token = account_details['user_token']
        self.business_token = account_details['business_token']


class Authentication(object):

    def __init__(self, auth_details):
        self.last_password_update_channel = auth_details['last_password_update_channel']
        self.last_password_update_time = datetime.strptime(auth_details['last_password_update_time'],
                                                           '%Y-%m-%dT%H:%M:%SZ')
        self.email_verified = auth_details['email_verified']
        self.email_verified_time = datetime.strptime(auth_details['email_verified_time'],'%Y-%m-%dT%H:%M:%SZ')




