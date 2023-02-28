<template>
<table id="tableComponent" class="table table-bordered table-striped">
  <thead>
    <tr>
      <th v-for="dia in dias" :key='dia'> 
        {{ dia }} <i class="bi bi-sort-alpha-down" aria-label='Sort Icon'></i>
      </th>
      <td scope="column">
        <font-awesome-icon  icon="fas fa-plus-circle" />
      </td>
    </tr>
  </thead>
  <tbody>
    <tr v-for="modulo in modulos" :id="modulo" font="bold">
      {{ modulo }}
      <th v-for="dia in dias" :id="dia + modulo" :class="{'highlight': (selectedCells.includes(dia+modulo))}" 
      @click="selectCell(dia + modulo)" @dragover="prevent($event)" @drop="onDrop($event, 'Lunes1')">
      {{ items.filter((item) => item.list === (dia+modulo)) }}
      </th>
    </tr>
    <td scope="row">
      <font-awesome-icon  icon="fas fa-plus-circle" />
    </td>
  </tbody>
</table>


<div>
  Módulos a repartir: {{ modulos_a_repartir }}
</div>

<br>
<br>
<br>
<br>

<div>{{ info }}</div>
<!-- 
  <div>
    <div class="drop-zone" @dragover="prevent($event)" @drop="onDrop($event, 'idle')">
      <div class="drag-el" v-for="item in listOne" :key="item.nombre" draggable="true" @dragstart="startDrag($event, item)">
        {{ item.nombre }}
      </div>
    </div>
  </div> -->



</template>
<script>
export default {
  name: 'TableComponent',
  props:{
      // 
      modulos:{
          type: Array,
      },
      dias:{
          type: Array,
      },
      info: {
        type: Array,
      }
  }, 
  data() {
   return {
       users: [],
       selectedCells: [],
       modulos_a_repartir: 38,
       items: [{nombre: 'Matemáticas', id: 1, list: 'idle'}, {nombre: 'Lenguaje', id: 2, list: 'idle'},{nombre: 'Inglés', id: 3, list: 'idle'}],
       itemID: 0
      //  ramos2: ['']
   }
  },
  computed: {
    listOne() {
      return this.items.filter((item) => item.list === 'idle')
    },
  },
  methods: {
    selectCell(id) {
      var idx = this.selectedCells.indexOf(id);
      if (idx > -1) {
        this.selectedCells.splice(idx,1)
        this.modulos_a_repartir = this.modulos_a_repartir + 1
      } else {
        if (this.modulos_a_repartir > 0) {
          this.selectedCells.push(id);
          this.modulos_a_repartir = this.modulos_a_repartir - 1
        }
      }
    },
    startDrag(evt, item) {
      evt.dataTransfer.dropEffect = 'move'
      evt.dataTransfer.effectAllowed = 'move'
      this.itemID = item.id
    },
    onDrop(evt, list) {
      evt.dataTransfer.dropEffect = 'move'
      var itemID = this.itemID;
      const item = this.items.find((item) => item.id == itemID)
      item.list = list
    },
    prevent(evt) {
      evt.preventDefault()
    }
  }
}
</script>

<style>
#tableComponent {
  width: 100%;
}

#tableComponent {
  font-family: Arial, Helvetica, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

#tableComponent td, #tableComponent th {
  border: 1px solid #ddd;
  padding: 8px;
}

#tableComponent tbody tr {
  height: 40px;
  text-align: center;
  vertical-align: middle;
  line-height: 40px;
}

#tableComponent td:first-child {
  width: 5%;
}

#tableComponent tr:nth-child(even){background-color: #f2f2f2;}

#tableComponent thead {
  padding-top: 12px;
  padding-bottom: 12px;
  text-align: left;
  background-color: #04AA6D;
  color: white;
  text-align: center;
}

.highlight {
     background-color: grey;
}

tr:hover{
     cursor: pointer;
}
.drop-zone {
  background-color: #eee;
  margin-bottom: 10px;
  padding: 30px;
}
.drag-el {
  background-color: #fff;
  margin-bottom: 10px;
  padding: 10px;
}
</style>