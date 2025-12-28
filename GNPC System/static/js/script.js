// document.addEventListener("DOMContentLoaded", () => {

//     /* ==========================
//        CHART INITIALIZATION
//     ========================== */
//     const chartCanvas = document.getElementById("opsChart");

//     if (!chartCanvas) return;

//     const opsChart = new Chart(chartCanvas, {
//         type: "bar",
//         data: {
//             labels: [
//                 "Upstream",
//                 "Midstream",
//                 "Downstream",
//                 "Environmental"
//             ],
//             datasets: [{
//                 label: "Operational Records",
//                 data: [0, 0, 0, 0], // dynamically updated
//                 backgroundColor: [
//                     "#0a2540",   // GNPC Blue
//                     "#f5c400",   // GNPC Yellow
//                     "#1565c0",   // Deep Blue
//                     "#2e7d32"    // Environmental Green
//                 ],
//                 borderRadius: 6
//             }]
//         },
//         options: {
//             responsive: true,
//             plugins: {
//                 legend: {
//                     display: false
//                 },
//                 title: {
//                     display: true,
//                     text: "Operational Distribution by Sector"
//                 }
//             },
//             scales: {
//                 y: {
//                     beginAtZero: true,
//                     ticks: {
//                         precision: 0
//                     }
//                 }
//             }
//         }
//     });

//     /* ==========================
//        DATA EXTRACTION FROM TABLE
//     ========================== */
//     function updateChartFromTable(filter = "All") {
//         const rows = document.querySelectorAll("tbody tr");

//         const counts = {
//             Upstream: 0,
//             Midstream: 0,
//             Downstream: 0,
//             Environmental: 0
//         };

//         rows.forEach(row => {
//             const categoryCell = row.children[2];
//             if (!categoryCell) return;

//             const category = categoryCell.textContent.trim();

//             if (filter === "All" || category === filter) {
//                 if (counts[category] !== undefined) {
//                     counts[category]++;
//                 }
//             }

//             // hide rows based on filter
//             row.style.display =
//                 filter === "All" || category === filter
//                     ? ""
//                     : "none";
//         });

//         opsChart.data.datasets[0].data = [
//             counts.Upstream,
//             counts.Midstream,
//             counts.Downstream,
//             counts.Environmental
//         ];

//         opsChart.update();
//     }

//     /* ==========================
//        FILTER BUTTON HANDLERS
//     ========================== */
//     document.querySelectorAll(".filters button").forEach(button => {
//         button.addEventListener("click", () => {
//             const category = button.textContent.trim();
//             updateChartFromTable(category);
//         });
//     });

//     /* ==========================
//        INITIAL LOAD
//     ========================== */
//     updateChartFromTable("All");

// });

document.addEventListener("DOMContentLoaded", function () {

    const canvas = document.getElementById("opsChart");

    // Stop if canvas is missing
    if (!canvas) {
        console.error("opsChart canvas not found");
        return;
    }

    new Chart(canvas, {
        type: "bar",
        data: {
            labels: ["Upstream", "Midstream", "Downstream", "Environmental"],
            datasets: [{
                label: "Operational Distribution",
                data: [4, 3, 5, 2], // TEMP DATA (for visibility)
                backgroundColor: [
                    "#0a2540",
                    "#f5c400",
                    "#1565c0",
                    "#2e7d32"
                ],
                borderRadius: 6
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    display: true
                }
            },
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });

});

function filterRecords(category) {
    const rows = document.querySelectorAll("#operationsTable tr");

    rows.forEach(row => {
        const rowCategory = row.getAttribute("data-category");

        if (category === "All" || rowCategory === category) {
            row.style.display = "";
        } else {
            row.style.display = "none";
        }
    });
}
