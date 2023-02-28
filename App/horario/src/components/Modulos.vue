<template>
  <input v-model="current_curso" list="cursos">
  <datalist id="cursos">
    <option v-for="tupla in tuplas">{{ tupla.curso }}</option>>
  </datalist>
  <button v-bind:disabled="disable(current_curso)" @click="addNewClass(current_curso)">+</button>
  <h1>{{ title }} {{ current_curso }} (Programa educacional: {{ programa }})</h1>
  <table id="info">
    <tr>
      <td></td>
      <td>Ramo</td>
      <td>Profesor</td>
      <td>Módulos semanales</td>
      <td>Máximo de módulos diarios</td>
      <td>Comportamiento módulos diarios</td>
    </tr>
    <tr v-for="(tupla, k) in tuplas_curso_actual" :key="k">
      <td scope="row" class="trashIconContainer">
        <font-awesome-icon v-if="this.tuplas_curso_actual.length > 1" icon="fa-solid fa-trash" @click="deleteRow(tupla)"/>
      </td>
      <td>
        <input :id="generarIdRamo(k)" list="ramos" type="text" v-model="tupla.ramo" v-on:change="anadirRamo">
        <datalist id="ramos">
          <option v-for="ramo in ramos">{{ ramo }}</option>
        </datalist>
      </td>
      <td >
        <div class="multiprof">
          <input v-for="(tupla2,l) in tupla.profesores" :key="l" :id="generarIdProf(k,l)" list="profesores" type="text" v-model="tupla2.name" v-on:change="anadirProf"/>
          <datalist id="profesores">
            <option v-for="prof in profesores">{{ prof }}</option>
          </datalist>
        </div>
        <br>
        <button v-bind:disabled="isDisabledProf(k)" @click="addNewProf(k,l)">
          <font-awesome-icon icon="fas fa-plus-circle"/>
        </button>
        <button v-if="this.tuplas_curso_actual[k].profesores.length > 1" @click="deleteProf(k)">
          <font-awesome-icon icon="fa-solid fa-trash"/>
        </button>
      </td>
      <td>
        <input class="form-control" type="number" min="1" step="1" v-model="tupla.cantidad_modulos">
      </td>
      <td>
        <input class="form-control2" type="number" min="1" :max="calcularMax(k)" step="1" v-model="tupla.maximo_diario">
      </td>
      <td>
        <select v-if="this.tuplas_curso_actual[k].maximo_diario > 1" v-model="tupla.tipo_modulos">
          <option v-for="tipo in opciones_tipo_modulos">{{ tipo }}</option>
        </select>
      </td>
    </tr>
  </table> 
  
  <!-- <td>
    <input :id="generarIdProf(k)" list="profesores" type="text" v-model="tupla.profesor" v-on:change="anadirProf" />
    <datalist id="profesores">
      <option v-for="prof in profesores">{{ prof }}</option>
    </datalist>
  </td> -->

  <button v-bind:disabled="isDisabled(tuplas)" type='button' class="btn btn-info" @click="addNewRow(current_curso)">
      <font-awesome-icon icon="fas fa-plus-circle"/>
  </button>

  <br>
  <button v-on:click.prevent="cambiar_vista()">Armar horario</button>
</template>

<script>

export default {
  emits: ['actualizar_data'],
  data() {
    return {
      title: 'Ingrese las clases para el curso ',
      programa: 'XYZ',
      opciones_tipo_modulos: ['Sin preferencia', 'Módulos seguidos', 'Módulos disjuntos'],
      tuplas: [{
        curso: '',
        ramo: '',
        profesores: [{name: ''}],
        cantidad_modulos: 1,
        maximo_diario: 1,
        tipo_modulos: 'Sin preferencia'
      }],
      current_curso: '',
      ramos: [],
      profesores: [],
    }
  },
  methods: {
    addNewClass(current_curso) {
      this.tuplas.push({
          curso: current_curso,
          ramo: '',
          profesores: [{name: ''}],
          cantidad_modulos: 1,
          maximo_diario: 1, 
          tipo_modulos: 'Sin preferencia'
      });
    },
    addNewRow(current_curso) {
      this.tuplas.push({
          curso: current_curso,
          ramo: '',
          profesores: [{name: ''}],
          cantidad_modulos: 1,
          maximo_diario: 1, 
          tipo_modulos: 'Sin preferencia'
      });
      console.log(this.tuplas)
    },
    addNewProf(k,l) {
      this.tuplas_curso_actual[k].profesores.push({
        name: ''
      });
      console.log(this.tuplas_curso_actual[k])
    },
    calcularMax(k) {
      var max = this.tuplas_curso_actual[k].cantidad_modulos
      return max
    },
    check_one(k, string) {
      if (this.selected != []) {
        this.selected = []
      };
    },
    deleteProf(k) {
      var last_idx = this.tuplas_curso_actual[k].profesores.length - 1
      if (last_idx > -1) {
        this.tuplas_curso_actual[k].profesores.splice(last_idx, 1);
      };
    },
    deleteRow(tupla) {
      var idx = this.tuplas_curso_actual.indexOf(tupla);
      if (idx > -1) {
        this.tuplas_curso_actual.splice(idx, 1);
      }
    },
    disable(current_curso) {
      return current_curso === ''
    },
    isDisabled(tuplas) {
      var last_index = this.tuplas.length - 1;
      return this.tuplas[last_index].ramo === ""
    },
    isDisabledProf(k) {
      var last_index = this.tuplas_curso_actual[k].profesores.length - 1
      return this.tuplas_curso_actual[k].profesores[last_index].name === ""
    },
    generarIdProf(key, l) {
      return 'profesor' + key + '-' + l
    },
    generarIdRamo(key) {
      return 'ramo' + key
    },
    anadirProf: function(event) {
      if (!(this.profesores.includes(event.target.value))) {
        this.profesores.push(event.target.value);
      };
    },
    anadirRamo: function(event) {
      if (!(this.ramos.includes(event.target.value))) {
        this.ramos.push(event.target.value);
      };
    },
    cambiar_vista() {
      this.$emit("actualizar_data", this.tuplas)
    }
  },
  computed: {
    tuplas_curso_actual: function () {
      return this.tuplas.filter(i => i.curso === this.current_curso)
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

#info {
  font-family: Arial, Helvetica, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

#info td, #info th {
  border: 1px solid #ddd;
  padding: 8px;
}

#info td:first-child {
  width: 5%;
}

#info td:nth-child(3) {
  width: 10%;
}

#info tr:nth-child(even){background-color: #f2f2f2;}

#info tr:hover {background-color: #ddd;}

#info tr:first-child {
  padding-top: 12px;
  padding-bottom: 12px;
  text-align: left;
  background-color: #04AA6D;
  color: white;
  text-align: center;
}

input {
  text-align: center;
}

.multiprof{
  /* text-align: center; */
  display: flex;
  justify-content: center;
  flex-flow: row wrap;
  width: 100%;
}

input[type="text"] {
  text-align: left;
}

input[type="number"] {
  text-align: right;
  width: 30px;
}

input[type=number]::-webkit-inner-spin-button {
    opacity: 1
}
</style>