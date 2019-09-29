<template>
    <v-container>

    </v-container>
</template>

<script>
    import axios from 'axios'
    import store from '../store'
    export default {
        name: "First",
        data () {
            return {
                records: [],
                userName: null,
                isAdmin: false
            }
        },
        mounted () {
            this.updateUser()
            this.updateRecords()
        },
        methods: {
            updateRecords: function () {
                axios
                    .get(store.state.apiUrl + 'records', {
                        headers: {
                            Authorization: localStorage.token
                        }})
                    .then(response => {
                        this.records = response.data.data
                    })
            },
            updateUser: function () {
                this.userName = localStorage.userName
                this.isAdmin = localStorage.isAdmin
            }
        }
    }
</script>

<style scoped>

</style>
