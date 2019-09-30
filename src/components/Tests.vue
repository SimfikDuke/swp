<template>
    <v-container>
        <v-card width="600" style="margin-right: auto; margin-left: auto">
            <v-card-title>
                Тест здоровья
            </v-card-title>
            <v-card-text>
                <v-container v-if="state < 3" style="padding: 10%;">
                    <v-row>
                        <h2>{{ questions[state] }}</h2>
                    </v-row>
                    <v-row>
                        <v-radio-group>
                            <v-radio
                                    v-for="n in [0, 1, 2]"
                                    :key="n"
                                    :label="variants[state][n]"
                                    :value="rates[state][n]"
                                    @change="lastSelected = n"
                            ></v-radio>
                        </v-radio-group>
                    </v-row>
                </v-container>
                <v-container v-else>
                    <v-row>
                        <h1>Результат</h1>
                    </v-row>
                    <v-row>
                        <br>
                    </v-row>
                    <v-row>
                        <v-card>
                            <v-img
                                    max-width=400
                                    max-height=350
                                    :src="getResult()[1]">
                            </v-img>
                        </v-card>
                    </v-row>
                    <v-row>

                        <h2><br>{{ getResult()[0] }}</h2>
                    </v-row>
                </v-container>
            </v-card-text>
            <v-card-actions>
                <v-btn v-if="state < 2" @click="nextTest" :disabled="lastSelected === -1">Далее</v-btn>
                <v-btn v-else-if="state < 3" @click="nextTest" :disabled="lastSelected === -1">Результат</v-btn>
                <v-btn v-el        </v-card-actions>
        </v-card>
    </v-container>
</template>

<script>
    export default {
        name: "Tests",
        data () {
            return {
                questions: [
                    'Какой фрукт вы любите?',
                    'Какой вид деятельности предпочитаете?',
                    'Какой фрукт вы любите?'
                ],
                variants: [
                    ['Хурма', 'Яблоко', 'Банан'],
                    ['Бег', 'Компьютерные игры', 'Шахматы'],
                    ['Картошка', 'Огурец', 'Морковка']
                ],
                rates: [
                    [1, 2, -1],
                    [3, -4, -1],
                    [-3, 1, 3]
                ],
                lastSelected: -1,
                state: 0,
                sum: 0
            }
        },
        methods: {
            nextTest: function () {
                if (this.state < 3) {
                    this.sum += this.rates[this.state][this.lastSelected]
                    this.state += 1
                } else {
                    this.state = 0
                }
            },
            getResult: function () {
                if (this.sum < -1) {
                    return ['Нужно серьёзно подумать над образом жизни',
                        'https://www.volyn24.com/img/modules/news/5/8e/b77752f37f7194036c5be104173d28e5/gallery-photo.jpg']
                } else if (this.sum < 2) {
                    return ['Сейчас все хорошо, но нужно подумать над образом жизни',
                        'https://img11.postila.ru/data/e0/cc/84/11/e0cc841188b63bbcb512c12e114db5e51b125f7878dfc7d6c8e45c9f45de979b.jpg']
                } else {
                    return ['Вы будете здоровым',
                        'https://folkextreme.ru/wp-content/uploads/2019/07/fizicheskaya-forma-1.jpeg']
                }
            },
        }
    }
</script>

<style scoped>

</style>
