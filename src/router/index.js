import Router from 'vue-router'
import First from "../components/First";
import Main from "../components/Main";
import Vue from 'vue'


Vue.use(Router)

export default new Router({
    routes: [
        {
            path: '/',
            name: 'Main',
            component: Main
        },
        {
            path: '/first',
            name: 'First',
            component: First
        }
    ]
})
