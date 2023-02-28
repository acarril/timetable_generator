<template>
  <button v-on:click.prevent="post">POST</button>
</template>

<script>
import axios from 'axios'
export default {
  data() {
    return {
      title: 'asdfasd'
    }
  },
  methods: {
    hola() {
      console.log('asdfasdfas');
    },
    post: function() {
      axios.get('https://jsonplaceholder.typicode.com/posts')
      .then((response) => {
        console.log(response.data)
      })
      .catch()
    }
  } 
}
</script>