<template>
  <div class="outside"
    v-bind:class="{ 'ingroup': ingroup, 'not-ingroup': (ingroup == false) }">
    <h4 class="name">{{username}}
      <span class="action btn"
        v-on:click="toggle">
        <fa icon="times" v-if="ingroup"/>
        <fa icon="plus" v-else/>
      </span>
    </h4>
  </div>
</template>

<script>
export default {
  name: 'friend',
  data() {
    return {
      ingroup: false,
    };
  },
  props: {
    username: String,
  },
  methods: {
    toggle() {
      if (!this.ingroup) {
        this.$eventHub.$emit("create-user-added", this.username);
        this.ingroup = true;
      } else {
        this.$eventHub.$emit("create-user-removed", this.username);
        this.ingroup = false;
      }
    },
    checkIn(user) {
      if (user == this.username) {
        this.ingroup = true;
      }
    },
    checkOut(user) {
      if (user == this.username) {
        this.ingroup = false;
      }
    }
  },
  components: {
  },
  created() {
    this.$eventHub.$on("create-user-added", this.checkIn);
    this.$eventHub.$on("create-user-removed", this.checkOut);
  },
  beforeDestroy() {
    this.$eventHub.$off("create-user-added");
    this.$eventHub.$off("create-user-removed");
  },
};
</script>

<style>
.outside {
  width: 100%;
  height: 40px;
  overflow-y: wrap;
}

.not-ingroup {
  border: solid 1px rgb(240,240,240);
  background-color: white;
  overflow-y: wrap;
}

.ingroup {
  border: solid 1px rgb(190,180,190);
  background-color: rgb(235,230,235);
  overflow-y: wrap;
}

.name {
  margin-left: 40px;
  margin-top: 5px;
  margin-bottom: 5px;
  height: 30px;
}

.action {
  float: right;
  margin-top: -6px;
  border-radius: 0px;
  height: 40px;
  width: 40px;
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
