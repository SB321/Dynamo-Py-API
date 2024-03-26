var API_ENDPOINT = "https://(ADD_API).amazonaws.com/prod"

$(document).ready(function() {
  
  getEmployees();
});

document.getElementById("createEmployeeForm").onsubmit = function(event) {
  event.preventDefault(); 
  var inputData = {
    "employeeId": $('#id').val(),
    "name": $('#name').val(),
    "email": $('#email').val(),
    "address": $('#address').val(),
    "phone": $('#phone').val()
  };

  $.ajax({
    url: API_ENDPOINT,
    type: 'POST',
    data: JSON.stringify(inputData),
    contentType: 'application/json; charset=utf-8',
    success: function(response) {
      $('#createEmployeeForm')[0].reset();
      alert("success");


      getEmployees();
    },
    error: function() {
      alert("error");
    }
  });
};


function deleteEmployee(employeeId) {
  var requestBody = {
    "employeeId": employeeId.toString()
  };
  $.ajax({
    url: API_ENDPOINT,
    type: 'DELETE',
    data: JSON.stringify(requestBody),
    contentType: 'application/json; charset=utf-8',
    success: function(response) {
      alert("Employee deleted successfully");
      
      getEmployees();
    },
    error: function() {
      alert("Error deleting employee");
    }
  });
}


document.getElementById("getEmployees").onclick = function() {
  getEmployees();
};

function getEmployees() {
  $.ajax({
    url: API_ENDPOINT,
    type: 'GET',
    contentType: 'application/json; charset=utf-8',
    success: function(response) {
      $('#EmployeesTable tr').slice(1).remove();
      var data = JSON.parse(response.body); 
      data.forEach(function(employee) {
        var row = "<tr> \
          <td>" + employee.employeeId + "</td>\
          <td>" + employee.name + "</td>\
          <td>" + employee.email + "</td>\
          <td>" + employee.address + "</td>\
          <td>" + employee.phone + "</td>\
          <td>\
            <a href='#' class='delete' data-toggle='modal' onclick='deleteEmployee(" + employee.employeeId + ")'><i class='material-icons' data-toggle='tooltip' title='Delete'>&#xE872;</i></a>\
          </td>\
        </tr>";
        $("#EmployeesTable").append(row);
      });
    },
    error: function() {
      alert("Error fetching employees");
    }
  });
}
