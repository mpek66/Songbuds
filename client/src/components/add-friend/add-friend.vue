<template>
  <div>
    <ul class="list-group list-group-flush">
      <friend
        v-on:add="add"
        v-on:remove="remove"></friend>
      <friend></friend>
    </ul>
  </div>
</template>

<script>
import Friend from './friend';

export default {
  name: 'add-friend',
  data() {
    return {
      username: "",
    };
  },
  props: {
  },
  methods: {
    add(username) {
      this.$emit("add",username);
    },
    remove(username) {
      this.$emit("remove",username);
    }
  },
  components: {
    "friend": Friend,
  },
  created() {
  },
  beforeDestroy() {
  },
};
</script>

<style>
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
