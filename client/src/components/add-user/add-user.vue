<template>
  <div style="width: 100%">
    <div class="user-input btn-group" style="width: 100%">
      <input class="form-control" placeholder="Enter username"
        v-model="username"
        v-on:keyup.enter="add">
      <div class="btn btn-member" style="width: 40px; margin-left: -5px"
        v-on:click="add">
        <fa icon="plus" />
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'add-user',
  data() {
    return {
      username: "",
    };
  },
  props: {
    event: {
      type: String,
      default: "add-user",
    },
  },
  methods: {
    add() {
      if(this.username != ""){
        this.$eventHub.$emit(this.event, this.username);
        this.username = "";
      }
    }
  },
  components: {
  },
  created() {
  },
  beforeDestroy() {
  },
};
</script>

<style>
.user-input {
  width: 100%;
  max-width: 300px;
}

.form-control:focus{
    border-color: #cccccc;
    -webkit-box-shadow: none;
    box-shadow: none;
}

.btn-member {
  color: #212529;
  background-color: #EBE6EB;
  border-color: #BEB4BE;
}

.btn-member:hover,
.btn-member:focus,
.btn-member:active,
.btn-member.active,
.open .dropdown-toggle.btn-member {
  color: #212529;
  background-color: #BEB4BE;
  border-color: #BEB4BE;
}

.btn-member.disabled {
  background-color: #EBE6EB;
  border-color: #BEB4BE;
}

.btn-member .badge {
  color: #EBE6EB;
  background-color: #212529;
}
</style>
