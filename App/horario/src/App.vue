<template>
  <Modulos v-if="vista_horario" @actualizar_data="update($event)"> </Modulos>
  <Horario v-if="!vista_horario" :modulos='modulos' :dias ="dias" :info="tuplas"/>
  <!-- <Requests /> -->
  <button v-if="!vista_horario" v-on:click.prevent="cambiar_vista">Agregar clases</button>
  <button v-on:click.prevent="post">POST</button> 
</template>

<script>
import Modulos from './components/Modulos.vue'
import Horario from './components/Horario.vue'
import Requests from './components/Requests.vue'
import axios from 'axios'

export default {
  name: 'App',
  components: { Modulos, Horario, Requests },
  data() {
    return {
      vista_horario: true,
      tuplas: [{
        curso: '',
        ramo: '',
        profesores: [{name: ''}],
        cantidad_modulos: 1,
        maximo_diario: 1,
        tipo_modulos: 'Sin preferencia'
      }],
      test: {body: this.tuplas},
    }
  },
  setup(){
    //An array of values for the data
    const modulos = [
      '1','2','3','4','5','6','7','8','9'
    ]
    const dias = [
      '','Lunes','Martes','Miércoles','Jueves','Viernes'
    ]
    return{modulos,dias}
  },
  methods: {
    post() {
      if (this.tuplas[0].curso === '') {
        this.tuplas.shift();
      };
      console.log(this.test);
      const json = JSON.stringify(this.test);
      axios
      .post('http://localhost:8000/test', json, {
        headers : {
          'Content-Type' : 'application/json',
          'Accept' : 'application/json'
        }
      })
      .then(response => 
        console.log(response.data)
      )
      .catch(error => console.log(error))
    },
    update(e) {
      this.tuplas = e;
      this.vista_horario = !this.vista_horario;
      return this.vista_horario
    }
  } 
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>