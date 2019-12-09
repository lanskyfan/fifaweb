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
            legend: {
                display:true,
                position:"top",
            },
            responsive: true,
            tooltips: {
                mode: 'label',
                enabled: true,
                callbacks: {
                    label: function(tooltipItem, data) {
                        var label = "";

                        label +=  data.labels[tooltipItem.index]+": ";
                        label += Math.round(tooltipItem.yLabel * 100) / 100;
                        return label;
                    },

                    footer: function(tooltipItem, data) {
                        var labels =  [
                            ["Vision will increase your ability to play accurate & intricate", "through balls to set up your team mates with scoring chances."],
                            ["A good Crossing attribute will increase the chances of finding", "your team mates & avoiding the opposition."],
                            ["A high Free Kick Accuracy increases your chances of avoiding", "the wall & beating the keeper from dead ball situations."],
                            ["The better your Short Passing the less likely it will be that", "your player misplaces passes."],
                            ["Increase your Long Passing to turn defence into attack with", "improved accuracy & more powerful lobbed passes."],
                            ["The higher your Curve rating the more bend & swerve you'll", "get on the ball when shooting & crossing."]
                            ];

                        return [labels[tooltipItem[0].index][0], labels[tooltipItem[0].index][1]];
                    }
                },
            legend:{
                position:'bottom'
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
                        var label = "";
                        label +=  data.labels[tooltipItem.index]+": ";
                        label += Math.round(tooltipItem.yLabel * 100) / 100;
                        return label;
                    },

                    footer: function(tooltipItem, data) {
                        var labels =  [
                            ["Agile players can turn quicker & are more likely to attempt", "spectacular headers volleys & bicycle kicks."],
                            ["A good Balance rating will reduce your chances", "of stumbling & falling when challenged by an opponent."],
                            ["Good reactions will allow you to latch onto", "loose balls & rebounds quicker than other players."],
                            ["The better your Ball Control the more likely your", "player will be to take a good first touch when receiving the ball."],
                            ["A good Dribbling rating will mean your player will", "keep tighter control of the ball when running at speed."],
                            ["This attribute determines at what distance the player", "with the ball starts feeling the pressure from the opponent."]
                            ];

                        return [labels[tooltipItem[0].index][0], labels[tooltipItem[0].index][1]];
                    }
                },
            legend:{
                position:'bottom'
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
                        var label = "";
                        label +=  data.labels[tooltipItem.index]+": ";
                        label += Math.round(tooltipItem.yLabel * 100) / 100;
                        return label;
                    },

                    footer: function(tooltipItem, data) {
                        var labels =  [
                            ["The higher your Jumping the more likely you'll", "be to beat opposition players to aerial balls."],
                            ["A good Stamina rating will increase the amount of time your", "player can spend sprinting during a game as well as improve recovery time."],
                            ["Strength will increase your chances of winning", "physical challenges with opposition players."],
                            ["Aggression will increase your chances of coming", "out on top in a 50/50 challenge with the opposition."],
                            ];

                        return [labels[tooltipItem[0].index][0], labels[tooltipItem[0].index][1]];
                    }
                },
            legend:{
                position:'bottom'
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
        type: 'horizontalBar',
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
                xAxes: [ {
                    ticks: {
                        beginAtZero: true
                    }
                                } ]
            },
            legend:{
                display:false
            },
            tooltips: {
                mode: 'label',
                enabled: true,
                callbacks: {
                    label: function(tooltipItem, data) {
                        var label = "";
                        label +=  data.labels[tooltipItem.index]+": ";
                        label += tooltipItem.xLabel;
                        return label;
                    },

                    footer: function(tooltipItem, data) {
                        var labels =  [
                            ["The higher the rating the better your player will position", "themselves by default following the ball going out of play."],
                            ["A good Finishing attribute will increase your chances", "of beating the keeper with shots inside the box."],
                            ["The higher your Shot Power the more venom you'll", "get on shots of any type & from any distance."],
                            ["The better your Long Shots the more likely you'll", "be to beat the keeper with shots from outside the box."],
                            ["A good rating will increase your chances of connecting & scoring", "with a Volley to leave the keeper helpless."],
                            ["A good rating will increase your chances of tucking", "away Penalties & give the keeper no chance."]
                            ];

                        return [labels[tooltipItem[0].index][0], labels[tooltipItem[0].index][1]];
                    }
                }
            }
        }
    } );
}

function bar_charts2_update_data(data){
    // single bar chart
    var ctx = document.getElementById( "singelBarChart2" );
    ctx.height = 150;
    var myChart = new Chart( ctx, {
        type: 'horizontalBar',
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
                xAxes: [ {
                    ticks: {
                        beginAtZero: true
                    }
                                } ]
            },
            legend:{
                display:false
            },
            tooltips: {
                mode: 'label',
                enabled: true,
                callbacks: {
                    label: function(tooltipItem, data) {
                        var label = "";
                        label +=  data.labels[tooltipItem.index]+": ";
                        label += tooltipItem.xLabel;
                        return label;
                    },

                    footer: function(tooltipItem, data) {
                        var labels =  [
                            ["Interception determines the ability to read", "the game and intercept passes."],
                            ["A good Heading Accuracy will increase your", "timing & improve your accuracy when heading at goal."],
                            ["Increasing your Marking attribute will improve the default", "position your player takes up when your team is not in possession of the ball."],
                            ["A good Standing Tackle rating will mean you are more", "likely to come out with the ball when putting your foot in."],
                            ["The higher the value the greater your", "chance of being successful with Sliding Tackles."],
                            ];

                        return [labels[tooltipItem[0].index][0], labels[tooltipItem[0].index][1]];
                    }
                }
            }
        }
    } );
}

function bar_charts3_update_data(data){
    // single bar chart
    var ctx = document.getElementById( "singelBarChart3" );
    ctx.height = 150;
    var myChart = new Chart( ctx, {
        type: 'horizontalBar',
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
                    borderColor: "rgba(238,238,0, 0.9)",
                    borderWidth: "0",
                    backgroundColor: "rgba(238,238,0, 0.5)"
                            }
                        ]
        },
        options: {
            legend:{
                display:false
            },
            scales: {
                xAxes: [ {
                    ticks: {
                        beginAtZero: true
                    }
                                } ]
            },
            tooltips: {
                mode: 'label',
                enabled: true,
                callbacks: {
                    label: function(tooltipItem, data) {
                        var label = "";
                        label +=  data.labels[tooltipItem.index]+": ";
                        label += tooltipItem.xLabel;
                        return label;
                    },

                    footer: function(tooltipItem, data) {
                        var labels =  [
                            ["Handling is an exclusive goalkeeper attribute used to measures", "how cleanly he catches the ball and does he hold on to it."],
                            ["Kicking is used to measures the length and accuracy of goal", "kicks, from out of the hands or on the ground."],
                            ["It is the GK’s ability to position himself correctly when saving shots.", "It also affects the way how a goalkeeper reacts to crosses."],
                            ["Reflexes stat is the agility of the goalkeeper when making a save.", "It determines how quickly the goalkeeper reacts to a shot on goal."],
                            ];

                        return [labels[tooltipItem[0].index][0], labels[tooltipItem[0].index][1]];
                    }
                }
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
            // console.log(data)
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
            // console.log(data)
        }
    )
}

// function fetch_similar_and_change(id1,id2) {
//     // console.log(234)
//     fetch("/" + id1 + "/" + id2 + "/similar_player_score").then(
//         function (response) {
//             return response.json()
//         }
//     ).then(
//         function (data) {
//             radar_charts2_update_data(data);
//             // console.log(data);
//         }
//     )
// }



(function ($) {
    "use strict";
    var id_value = parseInt(document.getElementById('empty').name)
    // var id_value1= parseInt(document.getElementById('empty1').name)

    // console.log(id_value)



    //radar chart
    fetch_data_and_change(id_value)
    // fetch_similar_and_change(id_value,id_value1)
    //polar chart
    fetch_passing_and_change(id_value)
    fetch_dribbling2_and_change(id_value)
    fetch_physical_and_change(id_value)

    //bar chart
    fetch_shooting_and_change(id_value)
    fetch_defending_and_change(id_value)
    fetch_gk_and_change(id_value)

} )( jQuery );
