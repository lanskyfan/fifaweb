function radar_charts2_update_data(data) {
    var ctx = document.getElementById( "radarChart2" );
    ctx.height = 160;
    var myChart = new Chart( ctx, {
        type: 'radar',
        data: {
            labels: [ "PAC",  "SHO", 
            "PAS", "DRI", "DEF", "PHY" ],
            datasets: [
                {
                    label: "Original Player",
                    data: data[0],
                    fill:true,
                    pointBackgroundColor:"rgba(180,180,180, 0.8)",
                    borderColor: "rgba(160,160,160, 0.8)",
                    borderWidth: "1",
                    backgroundColor: "rgba(160,160,160, 0.4)"
                            },
                 {
                     label: "Similar Player",
                     data: data[1],
                     pointBackgroundColor:"rgba(255, 0, 0, 0.8)",
                     borderColor: "rgba(255, 0, 0, 0.7)",
                     borderWidth: "1",
                     backgroundColor: "rgba(255, 0, 0, 0.2)"
                             }
                         ]
        },
        options: {
            legend: {
                position:"bottom",
            },
            scale: {
                angleLines: {
                    display: true,
                },
                ticks: {
                    beginAtZero: true
                }
            },
            tooltips: {
                mode: 'label',
                enabled: true,
                callbacks: {
                    label: function(tooltipItem, data) {
                        // var label = data.datasets[tooltipItem.datasetIndex].label || '';
                        // var label = tooltipItem.datasetIndex;
                        var label;
                        var labels =  [
                        "Pace",
                        "Shooting",
                        "Passing",
                        "Dribbling",
                        "Defending",
                        "Physical"
                        ];
                        
                        label = labels[tooltipItem.index] + ": ";
                        label += Math.round(tooltipItem.yLabel * 100) / 100;
                        
                        // return [label , labels[tooltipItem.index][0], labels[tooltipItem.index][1]];
                        return label;
                    }
                }    
            }    

        }
    });
}

function fetch_similar_and_change(id1,id2) {
    // console.log(234)
    fetch("/" + id1 + "/" + id2 + "/similar_player_score").then(
        function (response) {
            return response.json()
        }
    ).then(
        function (data) {
            radar_charts2_update_data(data);
            // console.log(data);
        }
    )
}

(function ($) {
    "use strict";
    var id_value = parseInt(document.getElementById('empty').name)
    var id_value1= parseInt(document.getElementById('empty1').name)


    console.log(id_value)
    console.log(id_value1)

    fetch_similar_and_change(id_value,id_value1)

} )( jQuery );