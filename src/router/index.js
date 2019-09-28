import Router from 'vue-router'
import First from "../components/First";
import HelloWorld from "../components/HelloWorld";
import Vue from 'vue'


Vue.use(Router)

export default new Router({
    routes: [
        {
            path: '/',
            name: 'HelloWorld',
            component: HelloWorld
        },
        {
            path: '/first',
            name: 'First',
            component: First
        }
    ]
})
