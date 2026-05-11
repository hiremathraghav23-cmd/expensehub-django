console.log("ExpenseHub Loaded");

/* Delete Confirmation */

function confirmDelete(){

    return confirm(
        "Are you sure you want to delete?"
    );
}

/* Chart */

const ctx = document.getElementById('expenseChart');

if(ctx){

    new Chart(ctx, {

        type: 'doughnut',

        data: {

            labels: [
                'Income',
                'Expense'
            ],

            datasets: [{

                label: 'Finance',

                data: [75, 25],

                borderWidth: 1
            }]
        },
    });
}