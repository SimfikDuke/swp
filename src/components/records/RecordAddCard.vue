<template>
    <v-card class="mx-auto" width="305px" style="margin: 12px">
        <v-card-title>Добавить запись</v-card-title>
        <v-card-text style="padding-bottom: 0">
            <v-text-field
                    v-model="title"
                    label="Заголовок"></v-text-field>
            <v-textarea
                    outlined
                    name="input-7-4"
                    label="Текст"
                    v-model="textMsg"
            ></v-textarea>
        </v-card-text>
        <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn @click="addRecord">Добавить</v-btn>
        </v-card-actions>
    </v-card>
</template>

<script>
    import axios from 'axios'
    import store from '@/store'
    export default {
        name: 'RecordAddCard',
        data () {
            return {
                title: '',
                textMsg: ''
            }
        },
        props: {
            callbackMethod: Function
        },
        mounted () {
        },
        methods: {
            addRecord: function () {
                axios
                    .post(store.state.apiUrl + 'records',
                        {
                            title: this.title,
                            text: this.textMsg
                        },
                        {
                            headers: {
                                Authorization: localStorage.token
                            }
                        })
                    .then(() => {
                        this.callbackMethod()
                    })
            }
        }
    }
</script>

<style scoped>
</style>
