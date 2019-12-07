function radar_charts_update_data(data) {
    var ctx = document.getElementById( "radarChart" );
    ctx.height = 160;
    var myChart = new Chart( ctx, {
        type: 'radar',
        data: {
            labels: [ "PAC",  "SHO", 
            "PAS", "DRI", "DEF", "PHY" ],
            datasets: [
                {
                    label: "Player",
                    data: data,
                    fill:true,
                    pointBackgroundColor:"rgba(0, 139, 69, 0.7)",
                    borderColor: "rgba(0, 194, 146, 0.7)",
                    borderWidth: "1",
                    backgroundColor: "rgba(0, 194, 146, 0.4)"
                            },
                //  {
                //      label: "Second player",
                //      data: [10,10,10,10,10,10,10],
                //      borderColor: "rgba(0, 194, 146, 0.7",
                //      borderWidth: "1",
                //      backgroundColor: "rgba(0, 194, 146, 0.5)"
                //              }
                         ]
        },
        options: {
            legend: {
                display:false,
            },
            scale: {
                angleLines: {
                    display: true,
                },
                ticks: {
                    beginAtZero: true
                }
            }

        }
    });
}

function polar_charts_update_data(data) {
    //polar chart
    var ctx = document.getElementById( "polarChart" );
    ctx.height = 150;
    var myChart = new Chart( ctx, {
        type: 'polarArea',
        data: {
            datasets: [ {
                data: data,
                backgroundColor: [
                    "rgba(84, 255, 159, 0.4)",
                    "rgba(0, 70, 50, 0.3)",
                    "rgba(46, 139, 87, 0.4)",
                    "rgba(100, 255, 0, 0.5)",
                    "rgba(0, 150, 146, 0.5)",
                    "rgba(0, 100, 150, 0.2)",
                                ]

                            } ],
            labels: [
                "Vision",
                "Crossing",
                "FK accuracy",
                "Short passing",
                "Long passing",
                "Curve"
                ]
        },
        options: {
            responsive: true,
            tooltips: {
                mode: 'label',
                enabled: true,
                callbacks: {
                    label: function(tooltipItem, data) {
                        // var label = data.datasets[tooltipItem.datasetIndex].label || '';
                        // var label = tooltipItem.datasetIndex;
                        var label = "";
                        // var labels =  [
                        //     ["Vision will increase your ability to play accurate & intricate", "through balls to set up your team mates with scoring chances."],
                        //     ["A good Crossing attribute will increase the chances of finding", "your team mates & avoiding the opposition."],
                        //     ["A high Free Kick Accuracy increases your chances of avoiding", "the wall & beating the keeper from dead ball situations."],
                        //     ["The better your Short Passing the less likely it will be that", "your player misplaces passes."],
                        //     ["Increase your Long Passing to turn defence into attack with", "improved accuracy & more powerful lobbed passes."],
                        //     ["The higher your Curve rating the more bend & swerve you'll", "get on the ball when shooting & crossing."]
                        //     ];

                        label +=  data.labels[tooltipItem.index]+": ";
                        label += Math.round(tooltipItem.yLabel * 100) / 100;
                        
                        // return [label , labels[tooltipItem.index][0], labels[tooltipItem.index][1]];
                        return label;
                    },

                    footer: function(tooltipItem, data) {
                        // var label = data.datasets[tooltipItem.datasetIndex].label || '';
                        // var label = tooltipItem.datasetIndex;
                        // var label = "";
                        var labels =  [
                            ["Vision will increase your ability to play accurate & intricate", "through balls to set up your team mates with scoring chances."],
                            ["A good Crossing attribute will increase the chances of finding", "your team mates & avoiding the opposition."],
                            ["A high Free Kick Accuracy increases your chances of avoiding", "the wall & beating the keeper from dead ball situations."],
                            ["The better your Short Passing the less likely it will be that", "your player misplaces passes."],
                            ["Increase your Long Passing to turn defence into attack with", "improved accuracy & more powerful lobbed passes."],
                            ["The higher your Curve rating the more bend & swerve you'll", "get on the ball when shooting & crossing."]
                            ];

                        // label +=  data.labels[tooltipItem.index]+": ";
                        // label += Math.round(tooltipItem.yLabel * 100) / 100;
                        // label += labels[tooltipItem.index]
                        return [labels[tooltipItem[0].index][0], labels[tooltipItem[0].index][1]];
                    }
                }
            }
        }
    } );
}

function polar_charts2_update_data(data) {
    //polar chart
    var ctx = document.getElementById( "polarChart2" );
    ctx.height = 150;
    var myChart = new Chart( ctx, {
        type: 'polarArea',
        data: {
            datasets: [ {
                data: data,
                backgroundColor: [
                    "rgba(255, 105, 180, 0.4)",
                    "rgba(255, 20, 147, 0.3)",
                    "rgba(255, 192, 203, 0.4)",
                    "rgba(219, 112,147, 0.5)",  
                    "rgba(176, 48, 96, 0.5)",
                    "rgba(186, 85, 211, 0.3)",
                                ]

                            } ],
            labels: [
                "Agility",
                "Balance",
                "Reactions",
                "Ball Control",
                "Dribbling",
                "Composure"
                ]
        },
        options: {
            responsive: true,
            tooltips: {
                mode: 'label',
                enabled: true,
                callbacks: {
                    label: function(tooltipItem, data) {
                        // var label = data.datasets[tooltipItem.datasetIndex].label || '';
                        // var label = tooltipItem.datasetIndex;
                        var label = "";
                        var labels =  [
                            ["1"],
                            ["1"],
                            ["1"],
                            ["1"],
                            ["1"],
                            ["1"]
                            ];

                        label +=  data.labels[tooltipItem.index]+": ";
                        label += Math.round(tooltipItem.yLabel * 100) / 100;
                        // label += labels[tooltipItem.index]
                        return [label , labels[tooltipItem.index][0], labels[tooltipItem.index][1]];
                    }
                }
            }
        }
    } );
}

function polar_charts3_update_data(data) {
    //polar chart
    var ctx = document.getElementById( "polarChart3" );
    ctx.height = 150;
    var myChart = new Chart( ctx, {
        type: 'polarArea',
        data: {
            datasets: [ {
                data: data,
                backgroundColor: [
                    "rgba(139, 69, 19, 0.4)",
                    "rgba(160, 82, 45, 0.3)",
                    "rgba(205, 133, 63, 0.4)",
                    "rgba(222, 184,135, 0.5)",  
                                ]

                            } ],
            labels: [
                "Jumping",
                "Stamina",
                "Strength",
                "Aggression",
                ]
        },
        options: {
            responsive: true,
            tooltips: {
                mode: 'label',
                enabled: true,
                callbacks: {
                    label: function(tooltipItem, data) {
                        // var label = data.datasets[tooltipItem.datasetIndex].label || '';
                        // var label = tooltipItem.datasetIndex;
                        var label = "";
                        var labels =  [
                            ["1"],
                            ["1"],
                            ["1"],
                            ["1"],
                            ];

                        label +=  data.labels[tooltipItem.index]+": ";
                        label += Math.round(tooltipItem.yLabel * 100) / 100;
                        // label += labels[tooltipItem.index]
                        return [label , labels[tooltipItem.index][0], labels[tooltipItem.index][1]];
                    }
                }
            }
        }
    } );
}

function bar_charts_update_data(data){
    // single bar chart
    var ctx = document.getElementById( "singelBarChart" );
    ctx.height = 150;
    var myChart = new Chart( ctx, {
        type: 'bar',
        data: {
            labels: [ "Positioning", 
            "Finishing", 
            "Shot Power", 
            "Long Shots", 
            "Volleys", 
            "Penalties", 
            ],
            datasets: [
                {
                    label: "Shooting",
                    data: data,
                    borderColor: "rgba(255, 0, 0, 0.9)",
                    borderWidth: "0",
                    backgroundColor: "rgba(255, 0, 0, 0.5)"
                            }
                        ]
        },
        options: {
            scales: {
                yAxes: [ {
                    ticks: {
                        beginAtZero: true
                    }
                                } ]
            }
        }
    } );
}

function bar_charts2_update_data(data){
    // single bar chart
    var ctx = document.getElementById( "singelBarChart2" );
    ctx.height = 150;
    var myChart = new Chart( ctx, {
        type: 'bar',
        data: {
            labels: [ "Interceptions", 
            "Heading Accuracy", 
            "Marking", 
            "Standing Tackle", 
            "Sliding Tackle",  
            ],
            datasets: [
                {
                    label: "Defending",
                    data: data,
                    borderColor: "rgba(99,184,255, 0.9)",
                    borderWidth: "0",
                    backgroundColor: "rgba(99,184,255, 0.5)"
                            }
                        ]
        },
        options: {
            scales: {
                yAxes: [ {
                    ticks: {
                        beginAtZero: true
                    }
                                } ]
            }
        }
    } );
}

function bar_charts3_update_data(data){
    // single bar chart
    var ctx = document.getElementById( "singelBarChart3" );
    ctx.height = 150;
    var myChart = new Chart( ctx, {
        type: 'bar',
        data: {
            labels: [  
            "GK Handling", 
            "GK Kicking", 
            "GK Positioning", 
            "GK Reflexes",  
            ],
            datasets: [
                {
                    label: "Goalkeeping",
                    data: data,
                    borderColor: "rgba(255,255,0, 0.9)",
                    borderWidth: "0",
                    backgroundColor: "rgba(255,255,0, 0.5)"
                            }
                        ]
        },
        options: {
            scales: {
                yAxes: [ {
                    ticks: {
                        beginAtZero: true
                    }
                                } ]
            }
        }
    } );
}

function fetch_data_and_change(id) {
    // console.log(234)
    fetch("/" + id + "/score").then(
        function (response) {
            return response.json()
        }
    ).then(
        function (data) {
            radar_charts_update_data(data);
            // console.log(data);
        }
    )
}

function fetch_passing_and_change(id) {
    // console.log(234)
    fetch("/" + id + "/passing").then(
        function (response) {
            return response.json()
        }
    ).then(
        function (data) {
            polar_charts_update_data(data);
            // console.log(data);
        }
    )
}

function fetch_shooting_and_change(id){
    fetch("/" + id + "/shooting").then(
        function (response) {
            return response.json()
        }
    ).then(
        function (data) {
            bar_charts_update_data(data);
        }
    )
}

function fetch_defending_and_change(id){
    fetch("/" + id + "/defending").then(
        function (response) {
            return response.json()
        }
    ).then(
        function (data) {
            bar_charts2_update_data(data);
            console.log(data)
        }
    )
}

function fetch_dribbling2_and_change(id){
    fetch("/" + id + "/dribbling2").then(
        function (response) {
            return response.json()
        }
    ).then(
        function (data) {
            polar_charts2_update_data(data);
        }
    )
}

function fetch_physical_and_change(id){
    fetch("/" + id + "/physical").then(
        function (response) {
            return response.json()
        }
    ).then(
        function (data) {
            polar_charts3_update_data(data);
        }
    )
}

function fetch_gk_and_change(id){
    fetch("/" + id + "/gk").then(
        function (response) {
            return response.json()
        }
    ).then(
        function (data) {
            bar_charts3_update_data(data);
            console.log(data)
        }
    )
}


(function ($) {
    "use strict";
    var id_value = parseInt(document.getElementById('empty').name)
    console.log(id_value)

    //radar chart
    fetch_data_and_change(id_value)

    //polar chart
    fetch_passing_and_change(id_value)
    fetch_dribbling2_and_change(id_value)
    fetch_physical_and_change(id_value)

    //bar chart
    fetch_shooting_and_change(id_value)
    fetch_defending_and_change(id_value)
    fetch_gk_and_change(id_value)

} )( jQuery );
