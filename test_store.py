from jsonschema import validate
import pytest
import requests
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
    # You can create unique test data for each run here if needed
    return {
               
        "id": 0, 
        "status": "placed"  
    }
              
                
           

def test_patch_order_by_id(unique_order_data):
    test_endpoint = f"/store/order/{unique_order_data['id']}"
    new_status = "approved" 
    
    response = api_helpers.patch_api_data(test_endpoint, data={"status": new_status})
   
    assert response.status_code == 200
    
    assert response.json()["message"] == "Order and pet status updated successfully"

   


