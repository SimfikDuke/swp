<template>
    <v-card class="mx-auto" width="305px" style="margin: 12px">
        <v-card-title>Добавить запись</v-card-title>
        <v-card-text style="padding-bottom: 0">
            <v-text-field label="Заголовок"></v-text-field>
            <v-textarea
                    outlined
                    name="input-7-4"
                    label="Текст"
            ></v-textarea>
        </v-card-text>
        <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn>Добавить</v-btn>
        </v-card-actions>
    </v-card>
</template>

<script>
    export default {
        name: 'RecordAddCard'
    }
</script>

<style scoped>
</style>
