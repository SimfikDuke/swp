<template>
    <v-card class="mx-auto" width="305px" style="margin: 12px">
        <v-card-title>{{ title }}</v-card-title>
        <v-card-text>
            <v-container class="commonContent">
                {{ text }}
            </v-container>
        </v-card-text>
        <v-card-actions>
            <span class="dateSpan">{{ date }}</span>
            <v-spacer></v-spacer>
            <span class="authorSpan">{{ author }}</span>
            <v-btn v-if="isAdmin" @click="deleteRecord" xx-small text icon><v-icon>mdi-delete</v-icon></v-btn>
        </v-card-actions>
    </v-card>
</template>

<script>
    import axios from 'axios'
    import store from '@/store'
    export default {
        name: 'RecordCard',
        props: {
            id: Number,
            title: String,
            text: String,
            date: String,
            author: String,
            isAdmin: Boolean,
            callbackMethod: Function
        },
        methods: {
            deleteRecord: function () {
                axios
                    .delete(store.state.apiUrl + 'records/' + this.id,
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
    .commonContent {
        margin: 1%;
        padding: 1%;
        min-height: 100px;
        max-height: 375px;
    }
    .downBottom {
        display: table-cell;
        vertical-align: bottom;
    }
    .dateSpan {
        color: rgba(91, 125, 154, 0.66);
        font-style: oblique;
        font-size: 11px;
    }
    .authorSpan {
        color: #2c3e50;
        font-style: oblique;
        font-size: 11px;
    }
</style>
