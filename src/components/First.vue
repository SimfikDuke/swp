<template>
    <v-container fluid>
        <v-sparkline
                :value="value"
                :gradient="gradient"
                :smooth="radius || false"
                :padding="padding"
                :line-width="lineWidth"
                :stroke-linecap="lineCap"
                :gradient-direction="gradientDirection"
                :fill="fill"
                :type="type"
                :auto-line-width="autoLineWidth"
                auto-draw
                :show-labels="showLabels"
                :label-size="labelSize"
        ></v-sparkline>

        <v-divider></v-divider>
        <v-row>
            <v-text-field @change="upd" v-model="inp"></v-text-field>
        </v-row>
        <v-divider></v-divider>

        <v-row>
            <v-col cols="12">
                <v-row class="fill-height" align="center">
                    <v-subheader class="pl-0">Тип</v-subheader>
                    <v-btn-toggle v-model="type" mandatory>
                        <v-btn small text value="bar">Полоски</v-btn>
                        <v-btn small text value="trend">Линия</v-btn>
                    </v-btn-toggle>
                </v-row>
            </v-col>

            <v-col cols="12" md="6">
                <v-row class="fill-height" align="center">
                    <v-subheader class="pl-0">Градиент</v-subheader>
                    <v-item-group v-model="gradient" mandatory>
                        <v-row>
                            <v-item
                                    v-for="(gradient, i) in gradients"
                                    :key="i"
                                    v-slot:default="{ active, toggle }"
                                    :value="gradient"
                            >
                                <v-card
                                        :style="{
                    background: gradient.length > 1
                      ? `linear-gradient(0deg, ${gradient})`
                      : gradient[0],
                    border: '2px solid',
                    borderColor: active ? '#222' : 'white'
                  }"
                                        width="30"
                                        height="30"
                                        class="mr-2"
                                        @click.native="toggle"
                                ></v-card>
                            </v-item>
                        </v-row>
                    </v-item-group>
                </v-row>
            </v-col>

            <v-col cols="12" md="6">
                <v-row class="fill-height" align="center">
                </v-row>
            </v-col>

            <v-col cols="12">
                <v-slider
                        v-model="lineWidth"
                        label="Ширина линии"
                        min="0.1"
                        max="10"
                        step="0.1"
                        thumb-label
                        :disabled="autoLineWidth"
                ></v-slider>
            </v-col>

            <v-col cols="12">
                <v-slider
                        v-model="radius"
                        label="Радиус округления"
                        min="0"
                        max="16"
                        thumb-label
                ></v-slider>
            </v-col>

            <v-col cols="12">
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
    const gradients = [
        ['#222'],
        ['#42b3f4'],
        ['red', 'orange', 'yellow'],
        ['purple', 'violet'],
        ['#00c6ff', '#F0F', '#FF0'],
        ['#f72047', '#ffd200', '#1feaea'],
    ]

    export default {
        name: "First",
        data: () => ({
            showLabels: true,
            lineWidth: 2,
            labelSize: 7,
            radius: 10,
            padding: 8,
            lineCap: 'round',
            gradient: gradients[5],
            inp: '0, 2, 5, 9, 5, 10, 3, 5, -4, -10, 1, 8, 2, 9, 0',
            value: [0, 2, 5, 9, 5, 10, 3, 5, -4, -10, 1, 8, 2, 9, 0],
            gradientDirection: 'top',
            gradients,
            fill: false,
            type: 'trend',
            autoLineWidth: false,
        }),
        methods: {
            upd: function () {
                var b = this.inp.split(',').map(function(item) {
                    return parseInt(item, 10);
                });
                this.value = b
            }
        }
    }
</script>

<style scoped>

</style>
