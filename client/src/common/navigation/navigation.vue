<template>
  <div style="height:50px; width: 100vw; position: fixed; top: 0px; left: 0px; z-index: 999">
    <b-navbar
      toggleable="sm"
      sticky="true">
      <b-navbar-brand href="#">Songbuds</b-navbar-brand>
      <b-navbar-toggle
        target="navCollapse">
      </b-navbar-toggle>
      <b-collapse is-nav id="navCollapse">
        <b-navbar-nav class="ml-auto">
          <b-nav-item to="home">Home</b-nav-item>
          <b-nav-item to="create">Create</b-nav-item>
          <b-nav-item to="party">Party</b-nav-item>
          <b-nav-item>Friends</b-nav-item>
          <b-nav-item>Account</b-nav-item>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
    <flash-notification></flash-notification>
  </div>
</template>

<script>
import FlashNotification from '@/common/flash/flash-notification';

export default {
  name: "navigation",
  components: {
    'flash-notification': FlashNotification,
  }
}

</script>

<style>
.navbar {
  background-color: #77438c;
}
.navbar .navbar-brand {
  color: #ecf0f1;
}
.navbar .navbar-brand:hover,
.navbar .navbar-brand:focus {
  color: #ecdbff;
}
.navbar .navbar-text {
  color: #ecf0f1;
}
.navbar .navbar-text a {
  color: #ecdbff;
}
.navbar .navbar-text a:hover,
.navbar .navbar-text a:focus {
  color: #ecdbff;
}
.navbar .navbar-nav .nav-link {
  color: #ecf0f1;
  border-radius: .25rem;
  margin: 0 0.25em;
}
.navbar .navbar-nav .nav-link:not(.disabled):hover,
.navbar .navbar-nav .nav-link:not(.disabled):focus {
  color: #ecdbff;
}
.navbar .navbar-nav .dropdown-menu {
  background-color: #77438c;
  border-color: #531f68;
}
.navbar .navbar-nav .dropdown-menu .dropdown-item {
  color: #ecf0f1;
}
.navbar .navbar-nav .dropdown-menu .dropdown-item:hover,
.navbar .navbar-nav .dropdown-menu .dropdown-item:focus,
.navbar .navbar-nav .dropdown-menu .dropdown-item.active {
  color: #ecdbff;
  background-color: #531f68;
}
.navbar .navbar-nav .dropdown-menu .dropdown-divider {
  border-top-color: #531f68;
}
.navbar .navbar-nav .nav-item.active .nav-link,
.navbar .navbar-nav .nav-item.active .nav-link:hover,
.navbar .navbar-nav .nav-item.active .nav-link:focus,
.navbar .navbar-nav .nav-item.show .nav-link,
.navbar .navbar-nav .nav-item.show .nav-link:hover,
.navbar .navbar-nav .nav-item.show .nav-link:focus {
  color: #ecdbff;
  background-color: #531f68;
}
.navbar .navbar-toggle {
  border-color: #531f68;
}
.navbar .navbar-toggle:hover,
.navbar .navbar-toggle:focus {
  background-color: #531f68;
}
.navbar .navbar-toggle .navbar-toggler-icon {
  color: #ecf0f1;
}
.navbar .navbar-collapse,
.navbar .navbar-form {
  border-color: #ecf0f1;
}
.navbar .navbar-link {
  color: #ecf0f1;
}
.navbar .navbar-link:hover {
  color: #ecdbff;
}

@media (max-width: 575px) {
  .navbar-expand-sm .navbar-nav .show .dropdown-menu .dropdown-item {
    color: #ecf0f1;
  }
  .navbar-expand-sm .navbar-nav .show .dropdown-menu .dropdown-item:hover,
  .navbar-expand-sm .navbar-nav .show .dropdown-menu .dropdown-item:focus {
    color: #ecdbff;
  }
  .navbar-expand-sm .navbar-nav .show .dropdown-menu .dropdown-item.active {
    color: #ecdbff;
    background-color: #531f68;
  }
}

@media (max-width: 767px) {
  .navbar-expand-md .navbar-nav .show .dropdown-menu .dropdown-item {
    color: #ecf0f1;
  }
  .navbar-expand-md .navbar-nav .show .dropdown-menu .dropdown-item:hover,
  .navbar-expand-md .navbar-nav .show .dropdown-menu .dropdown-item:focus {
    color: #ecdbff;
  }
  .navbar-expand-md .navbar-nav .show .dropdown-menu .dropdown-item.active {
    color: #ecdbff;
    background-color: #531f68;
  }
}

@media (max-width: 991px) {
  .navbar-expand-lg .navbar-nav .show .dropdown-menu .dropdown-item {
    color: #ecf0f1;
  }
  .navbar-expand-lg .navbar-nav .show .dropdown-menu .dropdown-item:hover,
  .navbar-expand-lg .navbar-nav .show .dropdown-menu .dropdown-item:focus {
    color: #ecdbff;
  }
  .navbar-expand-lg .navbar-nav .show .dropdown-menu .dropdown-item.active {
    color: #ecdbff;
    background-color: #531f68;
  }
}

@media (max-width: 1199px) {
  .navbar-expand-xl .navbar-nav .show .dropdown-menu .dropdown-item {
    color: #ecf0f1;
  }
  .navbar-expand-xl .navbar-nav .show .dropdown-menu .dropdown-item:hover,
  .navbar-expand-xl .navbar-nav .show .dropdown-menu .dropdown-item:focus {
    color: #ecdbff;
  }
  .navbar-expand-xl .navbar-nav .show .dropdown-menu .dropdown-item.active {
    color: #ecdbff;
    background-color: #531f68;
  }
}

.navbar-expand .navbar-nav .show .dropdown-menu .dropdown-item {
  color: #ecf0f1;
}
.navbar-expand .navbar-nav .show .dropdown-menu .dropdown-item:hover,
.navbar-expand .navbar-nav .show .dropdown-menu .dropdown-item:focus {
  color: #ecdbff;
}
.navbar-expand .navbar-nav .show .dropdown-menu .dropdown-item.active {
  color: #ecdbff;
  background-color: #531f68;
}
</style>
