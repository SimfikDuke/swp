<template>
  <v-container>
    <v-layout
      wrap
    >
      <v-flex v-if="isAdmin">
        <RecordAddCard/>
      </v-flex>
      <v-flex v-for="record in records" :key="record.id">
        <RecordCard
                :title="record.title"
                :text="record.text"
                :date="record.created_at"
                :author="record.user.name"
        />
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
  import axios from 'axios'
  import store from '../store'
  import RecordCard from "./records/RecordCard";
  import RecordAddCard from "./records/RecordAddCard";
  export default {
    name: "Main",
    components: {RecordAddCard, RecordCard},
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
