// var observer = new MutationObserver(function(mutations) {
//     if (document.getElementById('lastaddress')) {
//         console.log("Exist, lets do something");
//         $(document).ready( function () {
//             $('#myTable').DataTable();
//         } );
//         //We can disconnect observer once the element exist if we dont want observe more changes in the DOM
//     }   
// });
// console.log("start datatable")
// observer.observe(document.body, { //document.body is node target to observe
//     childList: true, //This is a must have for the observer with subtree
//     subtree: true //Set to true if changes must also be observed in descendants.
// });
$(document).ready(function () {
    $('#myTable').DataTable( { 
        processing: true,
        ajax : {
            type: "POST",
            url: "/api/v1/add/",
            dataType: "json"
        },
        "columns": [
            {   
                "data":"addressid", 
                    "render": function (addressid) {
                        return "<a href=address/" + parseInt(addressid) + ">" + addressid + "</a>";
                    }
            },
            {"data" : "firstname"},
            { "data": "lastname" }, { "data": "Company" },
            { "data": "Email" }, {"data" : "Category"}
            
        ],
    } );
})

$('myT')

