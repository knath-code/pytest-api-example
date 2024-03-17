from jsonschema import validate
import pytest
import requests
import uuid
import schemas
import api_helpers
from hamcrest import assert_that, contains_string, is_

'''
TODO: Finish this test by...
1) Creating a function to test the PATCH request /store/order/{order_id}
2) *Optional* Consider using @pytest.fixture to create unique test data for each run
2) *Optional* Consider creating an 'Order' model in schemas.py and validating it in the test
3) Validate the response codes and values
4) Validate the response message "Order and pet status updated successfully"
'''
#def test_patch_order_by_id():
  #  pass

@pytest.fixture
def unique_order_data():
    user_id = f"test_user_{uuid.uuid4().hex}"
    # You can create unique test data for each run here if needed
    return {   
       #"order_id": "user_id",           
       "order_id": "5822a554-edbd-40f9-a8f0-c183282a73a0", 
       "pet_id": 0                 
    }
              
                
           
def test_patch_order_by_id(unique_order_data):
    #url = f"http://localhost:5000/store/order/bea2599a-393e-4826-a0fd-edcc1ca92af3"
    url = f"http://127.0.0.1:5000/store/order/{unique_order_data['order_id']}"
    headers = { "accept": "application/json", "Content-Type": "application/json"}   

    payload = {
         "status" : "sold"         
        
    }
   
    response = requests.patch(url, json=payload, headers=headers)
   
    assert response.status_code == 200
   
    expected_message = "Order and pet status updated successfully"
    assert response.json()["message"] == expected_message



