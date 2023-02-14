<template>
  <!-- <Modulos /> -->
  <Horario :modulos='modulos' :dias ="dias"/>
</template>

<!-- <template>
    <div class="container text-center  mt-5 mb-5">
    <h1 class="mt-5 fw-bolder text-success "> Student's Database </h1>
     <div class="table-responsive my-5">

       <Horario :dias='dias' :modulos ="modulos"></Horario>
     </div>

</div>
</template> -->

<script>
import Modulos from './components/Modulos.vue'
import Horario from './components/Horario.vue'

export default {
  name: 'App',
  components: { Modulos, Horario },
  setup(){
    //An array of values for the data
    const modulos = [
      '1','2','3','4','5','6','7','8','9'
    ]
    const dias = [
      '','Lunes','Martes','Miércoles','Jueves','Viernes'
    ]
    return{modulos,dias}
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