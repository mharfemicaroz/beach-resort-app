<template :key="componentKey">
  <div class="container-fluid mt-3">
    <div class="row app-header">
      <div class="col-md-12">
        <div class="d-flex justify-content-between">
          <div>
            <a
              class="navbar-brand text-white align-middlev vv vv v vv v"
              href="#"
            >
              <div style="display: flex; align-items: center">
                <img
                  :src="`/src/assets/${this.APP_LOGO_NAME}`"
                  width="45"
                  height="45"
                  class="d-inline-block align-top"
                  alt="Logo"
                  style="margin-right: 10px"
                />
                <div class="icon-container" style="margin-right: 25px">
                  <span class="h4">Task Manager v 1.0 </span>
                  <a
                    href="#"
                    v-if="userdata.role === 'supervisor'"
                    class="btn btn-link text-decoration-none text-white"
                    @click="toggleModal('settings-modal')"
                    data-bs-toggle="tooltip"
                    data-bs-placement="top"
                    title="Show settings"
                  >
                    <i class="fa fa-bars" style="font-size: 24px"></i>
                  </a>
                </div>
                <span
                  class="search-bar-container"
                  style="margin-right: 10px; display: flex; align-items: center"
                >
                  <input
                    v-model="searchText"
                    type="text"
                    class="form-control"
                    placeholder="Search..."
                    style="margin-right: 5px"
                  />
                  <i class="fa fa-search"></i>
                </span>
              </div>
            </a>
          </div>

          <div class="d-flex justify-content-between icon-container">
            <div class="icon-wrapper">
              <a
                href="#"
                v-if="userdata.role === 'supervisor'"
                class="btn btn-link text-decoration-none text-white"
                @click="addNewTask"
              >
                <i class="fa fa-plus-circle" style="font-size: 24px"></i>
              </a>
              <a
                href="#"
                v-if="countBackLogTasks > 0 && userdata.role === 'supervisor'"
                class="btn btn-link text-decoration-none text-white"
                @click="moveTasktoNewday"
              >
                <i
                  class="fas fa-history position-relative"
                  style="font-size: 24px"
                >
                  <span
                    class="badge bg-danger position-absolute top-0 start-100 translate-middle"
                    style="font-size: 12px; transform: translate(50%, -50%)"
                  >
                    {{ countBackLogTasks }}
                  </span>
                </i>
              </a>
            </div>
            <div>
              <a
                v-if="!isToggleBox"
                href="#"
                class="btn btn-link text-white text-decoration-none timeline"
                @click="toggleTimeline"
              >
                <i
                  v-if="isToggleTimeline"
                  class="fas fa-layer-group"
                  style="font-size: 24px"
                ></i>
                <i
                  v-else
                  class="fas fa-object-ungroup"
                  style="font-size: 24px"
                ></i>
              </a>
            </div>
            <div
              v-if="isToggleTimeline"
              style="
                border-left: 1px solid whitesmoke;
                border-right: 1px solid whitesmoke;
              "
            >
              <a
                href="#"
                class="btn btn-link text-white text-decoration-none"
                @click="togglePersonBox"
              >
                <i class="fas fa-person" style="font-size: 24px"></i>
              </a>
              <a
                href="#"
                class="btn btn-link text-white text-decoration-none"
                @click="toggleTaskBox"
              >
                <i class="fas fa-list-check" style="font-size: 24px"></i>
              </a>
              <a
                href="#"
                class="btn btn-link text-white text-decoration-none"
                @click="toggleStatusBox"
              >
                <i class="fas fa-check-circle" style="font-size: 24px"></i>
              </a>
            </div>
            <div class="icon-wrapper">
              <a
                href="#"
                v-if="!isToggleTimeline"
                class="btn btn-link text-white text-decoration-none"
                @click="toggleBox"
              >
                <i
                  v-if="isToggleBox"
                  class="fas fa-chevron-up"
                  style="font-size: 18px"
                ></i>
                <i
                  v-else
                  class="fas fa-chevron-down"
                  style="font-size: 24px"
                ></i>
              </a>
            </div>
            <div>
              <a
                href="#"
                class="btn btn-link text-white text-decoration-none"
                @click="logOut"
              >
                <i
                  class="fa-solid fa-right-from-bracket"
                  style="font-size: 24px"
                ></i>
              </a>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="row">
      <div class="col-md-12">
        <div class="calendar-parent c-p mt-1">
          <calendar-view
            :items="calendarItems"
            :show-date="showDate"
            :time-format-options="{ hour: 'numeric', minute: '2-digit' }"
            :enable-drag-drop="true"
            :disable-past="disablePast"
            :disable-future="disableFuture"
            :show-times="showTimes"
            :date-classes="myDateClasses"
            :display-period-uom="displayPeriodUom"
            :display-period-count="displayPeriodCount"
            :starting-day-of-week="startingDayOfWeek"
            :class="themeClasses"
            :period-changed-callback="periodChanged"
            :current-period-label="useTodayIcons ? 'icons' : ''"
            :displayWeekNumbers="displayWeekNumbers"
            :enable-date-selection="true"
            :selection-start="selectionStart"
            :selection-end="selectionEnd"
            @date-selection-start="setSelection"
            @date-selection="setSelection"
            @date-selection-finish="finishSelection"
            @drop-on-date="onDrop"
            @click-date="onClickDay"
            @click-item="onClickItem"
          >
            <template #header="{ headerProps }">
              <calendar-view-header
                slot="header"
                :header-props="headerProps"
                @input="setShowDate"
              />
            </template>
          </calendar-view>
        </div>
      </div>
    </div>
    <div
      class="row task-box"
      :style="`width:${calcMeasure.innerWidth}; overflow-y: hidden; overflow-x: auto;`"
    >
      <div class="col-md-12">
        <div class="d-flex flex-row bd-highlight mb-3">
          <div
            class="p-0 m-0 bd-highlight"
            v-for="(item, index) in aggregateByDept"
            :key="index"
          >
            <div class="card c-h" style="width: 277px; height: 335px">
              <div
                class="card-header bg-light text-dark d-flex justify-content-between"
              >
                <h4>
                  <i
                    v-if="item.dept === 'Beach'"
                    class="fa fa-umbrella-beach mr-3 p-0"
                  ></i>
                  <i
                    v-else-if="item.dept === 'Housekeeping'"
                    class="fas fa-broom mr-3 p-0"
                  ></i>
                  <i
                    v-else-if="item.dept === 'Resto'"
                    class="fas fa-pizza-slice mr-3 p-0"
                  ></i>
                  <i
                    v-else-if="item.dept === 'Pools'"
                    class="fa-solid fa-person-swimming mr-3 p-0"
                  ></i>
                  <i
                    v-else-if="item.dept === 'Office'"
                    class="fas fa-building mr-3 p-0"
                  ></i>
                  <i
                    v-else-if="item.dept === 'Maintenance'"
                    class="fas fa-tools mr-3 p-0"
                  ></i>
                  <i
                    v-else-if="item.dept === 'Security'"
                    class="fas fa-shield-alt mr-3 p-0"
                  ></i>
                  {{ item.dept }}
                </h4>

                <button
                  class="btn text-white bg-danger"
                  style="font-size: small"
                >
                  {{ item.data.length }}
                </button>
              </div>
              <div
                class="card-body c-h"
                @dragover="handleDragover($event)"
                @drop="handleDragdrop($event, item, 'task')"
                style="
                  width: 277px;
                  height: 335px;
                  overflow-y: auto;
                  overflow-x: hidden;
                "
              >
                <ul class="list-group">
                  <li
                    class="list-group-item mb-1 list-item"
                    draggable="true"
                    @dragstart="handleDragstart($event, itemData, 'task')"
                    :class="[
                      `${
                        itemData.isCompleted
                          ? 'task-completed'
                          : itemData.status === 'Open'
                          ? 'task-open'
                          : itemData.status === 'In progress'
                          ? 'task-progress'
                          : itemData.status === 'Inspected'
                          ? 'task-inspected'
                          : ''
                      }`,
                    ]"
                    v-for="(itemData, index2) in item.data"
                    :key="index2"
                    @click="onBoxItemClick(itemData)"
                  >
                    <div class="d-flex justify-content-between">
                      <span class="list-txtdesc">{{ itemData.taskname }} </span>
                      <span v-if="itemData.isNotify" class="p-0 m-0">
                        <i
                          class="fa-solid fa-bell text-white wiggle-animation"
                          style="font-size: 18px"
                        ></i>
                      </span>
                      <span
                        v-if="
                          itemData.isNewMessage && checkLastMessage(itemData)
                        "
                        class="p-0 m-0"
                      >
                        <i
                          class="fa-solid fa-message text-white wiggle-animation"
                          style="font-size: 18px"
                        ></i>
                      </span>
                    </div>
                  </li>
                </ul>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div
      class="row status-box"
      :style="`width:${calcMeasure.innerWidth}; overflow-y: hidden; overflow-x: auto`"
    >
      <div class="col-md-12">
        <div class="d-flex flex-row bd-highlight mb-3">
          <div
            class="p-0 bd-highlight"
            v-for="(item, index) in aggregateByStatus"
            :key="index"
          >
            <div class="card c-h" style="width: 277px; height: 335px">
              <div
                class="card-header text-white d-flex justify-content-between"
                :class="[
                  `${
                    item.status === 'Open'
                      ? 'task-open'
                      : item.status === 'In progress'
                      ? 'task-progress'
                      : item.status === 'Inspected'
                      ? 'task-inspected'
                      : ''
                  }`,
                ]"
              >
                <h4>
                  <i class="fa-solid fa-info-circle mr-3 p-0"></i>&nbsp;{{
                    item.status
                  }}
                </h4>
                <button class="btn text-dark bg-light" style="font-size: small">
                  {{ item.data.length }}
                </button>
              </div>
              <div
                class="card-body c-h"
                @dragover="handleDragover($event)"
                @drop="handleDragdrop($event, item, 'status')"
                style="
                  width: 277px;
                  height: 335px;
                  overflow-y: auto;
                  overflow-x: hidden;
                "
              >
                <ul class="list-group">
                  <li
                    class="list-group-item mb-1 list-item"
                    draggable="true"
                    @dragstart="handleDragstart($event, itemData, 'status')"
                    :class="[
                      `${
                        itemData.isCompleted
                          ? 'task-completed'
                          : 'task-incomplete'
                      }`,
                    ]"
                    v-for="(itemData, index2) in item.data"
                    @click="onBoxItemClick(itemData)"
                    :key="index2"
                  >
                    <div class="d-flex justify-content-between">
                      <span class="list-txtdesc">{{ itemData.taskname }}</span>
                      <span v-if="itemData.isNotify" class="p-0 m-0">
                        <i
                          class="fa-solid fa-bell text-dark wiggle-animation"
                          style="font-size: 18px"
                        ></i>
                      </span>
                      <span
                        v-if="
                          itemData.isNewMessage && checkLastMessage(itemData)
                        "
                        class="p-0 m-0"
                      >
                        <i
                          class="fa-solid fa-message text-dark wiggle-animation"
                          style="font-size: 18px"
                        ></i>
                      </span>
                    </div>
                  </li>
                </ul>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div
      class="row person-box"
      :style="`width:${calcMeasure.innerWidth}; overflow-y: hidden; overflow-x: auto`"
    >
      <div class="col-md-12">
        <div class="d-flex flex-row bd-highlight mb-3">
          <div
            class="p-0 bd-highlight"
            v-for="(item, index) in aggregateByPerson"
            :key="index"
          >
            <div class="card c-h" style="width: 277px; height: 335px">
              <div
                class="card-header bg-light text-dark d-flex justify-content-between"
              >
                <h4>
                  <i class="fa-solid fa-user mr-3 p-0"></i>&nbsp;{{
                    item.person_name
                  }}
                </h4>

                <button
                  class="btn text-white bg-danger"
                  style="font-size: small"
                >
                  {{ item.data.length }}
                </button>
              </div>
              <div
                class="card-body c-h"
                @dragover="handleDragover($event)"
                @drop="handleDragdrop($event, item, 'person')"
                style="
                  width: 277px;
                  height: 335px;
                  overflow-y: auto;
                  overflow-x: hidden;
                "
              >
                <ul class="list-group">
                  <li
                    class="list-group-item mb-1 list-item"
                    draggable="true"
                    @dragstart="handleDragstart($event, itemData, 'person')"
                    :class="[
                      `${
                        itemData.isCompleted
                          ? 'task-completed'
                          : itemData.status === 'Open'
                          ? 'task-open'
                          : itemData.status === 'In progress'
                          ? 'task-progress'
                          : itemData.status === 'Inspected'
                          ? 'task-inspected'
                          : ''
                      }`,
                    ]"
                    v-for="(itemData, index2) in item.data"
                    @click="onBoxItemClick(itemData)"
                    :key="index2"
                  >
                    <div class="d-flex justify-content-between">
                      <span class="list-txtdesc">{{ itemData.taskname }}</span>
                      <span v-if="itemData.isNotify" class="p-0 m-0">
                        <i
                          class="fa-solid fa-bell text-white wiggle-animation"
                          style="font-size: 18px"
                        ></i>
                      </span>
                      <span
                        v-if="
                          itemData.isNewMessage && checkLastMessage(itemData)
                        "
                        class="p-0 m-0"
                      >
                        <i
                          class="fa-solid fa-message text-white wiggle-animation"
                          style="font-size: 18px"
                        ></i>
                      </span>
                    </div>
                  </li>
                </ul>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <div
    class="modal fade show"
    id="settings-modal"
    tabindex="-1"
    role="dialog"
    aria-labelledby="settings-modalLabel"
    style="display: none; padding-right: 17px"
    aria-modal="true"
  >
    <div class="modal-dialog" role="document">
      <div class="modal-content" style="">
        <div class="modal-header">
          <h4 class="modal-title" id="settings-modalLabel">Settings</h4>
          <button
            type="button"
            class="close"
            data-bs-dismiss="modal"
            aria-label="Close"
          >
            <span aria-hidden="true">&times;</span>
          </button>
        </div>
        <div class="modal-body">
          <div class="row">
            <div class="col-md-6">
              <div class="form-group">
                <label class="form-label">Period UOM</label>
                <div class="input-group">
                  <select class="form-select" v-model="displayPeriodUom">
                    <option>month</option>
                    <option>week</option>
                    <option>year</option>
                  </select>
                </div>
              </div>
              <div class="form-group">
                <label class="form-label">Period Count</label>
                <div class="input-group">
                  <select class="form-select" v-model="displayPeriodCount">
                    <option :value="1">1</option>
                    <option :value="2">2</option>
                    <option :value="3">3</option>
                  </select>
                </div>
              </div>
              <div class="form-group">
                <label class="form-label">Starting day of the week</label>
                <div class="input-group">
                  <select class="form-select" v-model="startingDayOfWeek">
                    <option
                      v-for="(d, index) in dayNames"
                      :key="index"
                      :value="index"
                    >
                      {{ d }}
                    </option>
                  </select>
                </div>
              </div>
              <div class="form-group form-check">
                <input
                  class="form-check-input"
                  type="checkbox"
                  v-model="useTodayIcons"
                />
                <label class="form-check-label"
                  >Use icon for today's period</label
                >
              </div>
              <div class="form-group form-check">
                <input
                  class="form-check-input"
                  type="checkbox"
                  v-model="displayWeekNumbers"
                />
                <label class="form-check-label">Show week number</label>
              </div>
              <div class="form-group form-check">
                <input
                  class="form-check-input"
                  type="checkbox"
                  v-model="showTimes"
                />
                <label class="form-check-label">Show times</label>
              </div>
              <div class="form-group">
                <label class="form-label">Themes</label>
              </div>
              <div class="form-group form-check">
                <input
                  class="form-check-input"
                  type="checkbox"
                  v-model="useDefaultTheme"
                />
                <label class="form-check-label">Default</label>
              </div>
              <div class="form-group form-check">
                <input
                  class="form-check-input"
                  type="checkbox"
                  v-model="useHolidayTheme"
                />
                <label class="form-check-label">Holidays</label>
              </div>
            </div>
            <div class="col-md-6">
              <div class="form-group">
                <table
                  class="table table-bordered table-striped"
                  style="word-wrap: break-word"
                >
                  <thead>
                    <tr>
                      <th scope="col" style="width: 70% !important">
                        Status <i class="fas fa-tasks align-icon"></i>
                      </th>
                      <th scope="col" style="width: 30% !important">
                        Color <i class="fas fa-palette align-icon"></i>
                      </th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td>
                        Open <i class="fas fa-folder-open align-icon"></i>
                      </td>
                      <td class="task-open bg-primary"></td>
                    </tr>
                    <tr>
                      <td>
                        In progress <i class="fas fa-spinner align-icon"></i>
                      </td>
                      <td class="task-progress bg-warning"></td>
                    </tr>
                    <tr>
                      <td>
                        Inspected <i class="fas fa-search align-icon"></i>
                      </td>
                      <td class="task-inspected bg-info"></td>
                    </tr>
                    <tr>
                      <td>
                        Completed <i class="fas fa-check-circle align-icon"></i>
                      </td>
                      <td class="task-completed bg-success"></td>
                    </tr>
                    <tr>
                      <td>
                        Incomplete
                        <i class="fas fa-times-circle align-icon"></i>
                      </td>
                      <td class="task-incomplete bg-danger"></td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
          </div>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-danger" data-bs-dismiss="modal">
            Close
          </button>
        </div>
      </div>
    </div>
  </div>

  <div
    class="modal fade"
    id="loadTaskModal"
    tabindex="-1"
    aria-labelledby="loadTaskModalLabel"
    aria-hidden="true"
  >
    <div
      :class="`modal-dialog ${
        userdata.role === 'supervisor' ? 'modal-lg' : ''
      }`"
    >
      <div class="modal-content p-3">
        <div class="modal-header">
          <div class="d-flex justify-content-between w-100">
            <div class="d-flex align-items-center">
              <button
                type="button"
                @click="completeTask"
                v-if="userdata.role === 'supervisor'"
                class="btn btn-primary"
                style="margin-right: 10px !important"
              >
                <i
                  v-if="!task.isCompleted"
                  class="fa-solid fa-check"
                  style="font-size: large"
                ></i>
                <i
                  v-else
                  class="fa-solid fa-arrow-rotate-left"
                  style="font-size: large"
                ></i>
              </button>
              <template v-if="userdata.role !== 'supervisor'">
                <button
                  type="button"
                  v-if="!task.isNotify"
                  @click="toggleNotify"
                  :class="!isNotify ? 'btn btn-primary' : 'btn btn-danger'"
                  style="margin-right: 60px !important"
                >
                  <i class="fa-solid fa-bell" style="font-size: large"></i>
                </button>
              </template>
              <template v-else>
                <button
                  type="button"
                  v-if="task.isNotify"
                  @click="toggleNotify"
                  :class="!isNotify ? 'btn btn-primary' : 'btn btn-danger'"
                  style="margin-right: 60px !important"
                >
                  <i
                    class="fa-solid fa-bell-slash wiggle-animation"
                    style="font-size: large"
                  ></i>
                </button>
              </template>

              <select
                v-show="false"
                v-if="!task.isCompleted"
                :disabled="task.isCompleted || userdata.role !== 'supervisor'"
                v-model="task.assign.person.name"
                class="form-select"
                @change="
                  updateTasks('assigned task to ' + task.assign.person.name)
                "
              >
                <option value="Staff">Staff</option>
                <option
                  v-for="item in taskMembers"
                  :key="index"
                  :value="item.username"
                >
                  {{ item.username }}
                </option>
              </select>
              <div class="row" v-else>
                <div class="col-md-2 d-flex align-items-center">
                  <span style="font-size: 28px">
                    <i class="fas fa-check-circle text-success"></i>
                  </span>
                </div>
                <div class="col-md-10">
                  <div class="row">
                    <span>
                      <strong>Completed</strong> by
                      {{ task.assign.person.name }}
                    </span>
                  </div>
                  <div class="row">
                    <span class="text-muted">on {{ task.completionDate }}</span>
                  </div>
                </div>
              </div>
            </div>
            <div>
              <!-- Button that triggers the dropdown -->
              <button
                type="button"
                v-if="userdata.role === 'supervisor'"
                class="btn btn-circle bg-light text-dark btn-dropdown"
                style="font-size: small"
                @click="toggleDropdown"
              >
                <i class="fa fa-ellipsis-h" aria-hidden="true"></i>
              </button>
              <!-- Dropdown menu -->
              <div
                class="dropdown"
                v-if="isDropdownVisible"
                style="position: absolute"
              >
                <div class="dropdown-menu show">
                  <a
                    class="dropdown-item"
                    href="#"
                    @click="
                      toggleDropdown();
                      duplicateItem();
                    "
                  >
                    <i class="fas fa-copy"></i> Duplicate
                  </a>
                  <a class="dropdown-item" href="#" @click="toggleDropdown">
                    <i class="fas fa-print"></i> Print Report
                  </a>
                  <a
                    class="dropdown-item"
                    href="#"
                    @click="
                      toggleDropdown();
                      deleteItem();
                    "
                  >
                    <i class="fas fa-trash"></i> Delete Task
                  </a>
                </div>
              </div>
              &nbsp;
              <!-- Second button -->
              <button
                type="button"
                class="btn btn-circle bg-light text-dark"
                style="font-size: small"
                data-bs-dismiss="modal"
              >
                <i class="fa fa-times" aria-hidden="true"></i>
              </button>
              &nbsp;
            </div>
          </div>
        </div>

        <div class="modal-body">
          <div v-if="task.isCompleted" class="row bg-light p-3">
            <div class="col-md-6" style="border-right: 1px solid white">
              <div class="row">
                <div class="col-md-2 d-flex align-items-center">
                  <span style="font-size: 28px">
                    <i class="fas fa-clock text-primary"></i>
                  </span>
                </div>
                <div class="col-md-10">
                  <div class="row">
                    <span class="text-muted"> Time to complete </span>
                  </div>
                  <div class="row">
                    <span
                      ><strong>{{
                        timeDiff(task.completionDate, task.startDate)
                      }}</strong></span
                    >
                  </div>
                </div>
              </div>
            </div>

            <div class="col-md-6" style="border-right: 1px solid white">
              <div class="row">
                <div class="col-md-2 d-flex align-items-center">
                  <span style="font-size: 28px">
                    <i class="fas fa-user text-primary"></i>
                  </span>
                </div>
                <div class="col-md-10">
                  <div class="row">
                    <span class="text-muted"> Assigned to </span>
                  </div>
                  <div class="row">
                    <span
                      ><strong>{{ task.assign.person.name }}</strong></span
                    >
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="row">
            <div :class="`col-md-${userdata.role === 'supervisor' ? 7 : 12}`">
              <div class="form-group row">
                <div class="col-sm-12">
                  <input
                    :disabled="task.isCompleted"
                    :readonly="userdata.role !== 'supervisor'"
                    type="text"
                    placeholder="Add task name"
                    class="form-control"
                    style="font-size: x-large; border: 0"
                    v-model="task.name"
                    required
                    autocomplete="off"
                    @change="updateTasks('changed task name to ' + task.name)"
                  />
                </div>
              </div>
              <div class="form-group row mt-2">
                <div class="col-sm-12">
                  <input
                    :disabled="task.isCompleted"
                    :readonly="userdata.role !== 'supervisor'"
                    type="text"
                    placeholder="Add task description"
                    class="form-control"
                    style="font-size: medium; border: 0; color: darkgray"
                    v-model="task.desc"
                    maxlength="64"
                    required
                    autocomplete="off"
                    @change="
                      updateTasks('changed task description to ' + task.desc)
                    "
                  />
                </div>
              </div>
              <div class="form-group">
                <textarea
                  :disabled="task.isCompleted"
                  class="form-control"
                  minlength="3"
                  maxlength="256"
                  placeholder="Add comment"
                  v-model="taskComment"
                  rows="5"
                ></textarea>
              </div>
              <div class="form-group mt-2 d-flex justify-content-end">
                <button
                  style="margin-right: 10px"
                  :disabled="task.isCompleted"
                  v-if="userdata.role !== 'supervisor'"
                  class="btn btn-circle"
                  @click="
                    newComment(
                      task.itemID,
                      task.assign.person.name,
                      'notified task is done.'
                    )
                  "
                >
                  <i class="fas fa-check"></i>
                </button>
                <button
                  style="margin-right: 10px"
                  :disabled="task.isCompleted"
                  v-if="userdata.role !== 'supervisor'"
                  class="btn btn-circle"
                  @click="
                    newComment(
                      task.itemID,
                      task.assign.person.name,
                      'notified for task completion follow-up.'
                    )
                  "
                >
                  <i class="fas fa-reply"></i>
                </button>
                <button
                  :disabled="task.isCompleted"
                  class="btn btn-circle"
                  @click="newComment(task.itemID, userdata.role, taskComment)"
                >
                  <i class="fas fa-arrow-right"></i>
                </button>
              </div>
              <div class="form-group mt-2">
                <div class="row">
                  <div
                    class="col-md-12"
                    style="height: 150px; overflow-y: auto"
                  >
                    <div class="row" v-for="item in sortedStates" :key="index">
                      <div class="col-md-1 d-flex align-items-center">
                        <span
                          :title="item.actor"
                          style="font-size: 12px"
                          class="btn btn-circle"
                          :class="
                            item.actor === 'Staff'
                              ? 'bg-warning'
                              : item.actor === 'supervisor-aide'
                              ? 'bg-success'
                              : item.actor === 'supervisor'
                              ? 'bg-danger'
                              : 'bg-primary'
                          "
                        >
                          <!-- <i class="fas fa-comment text-primary"></i> -->
                          {{
                            item.actor === "Staff"
                              ? "ST"
                              : item.actor === "supervisor-aide"
                              ? "SA"
                              : item.actor === "supervisor"
                              ? "SV"
                              : userdata.FirstName.toString().toUpperCase() +
                                userdata.LastName.toString().toUpperCase()
                          }}
                        </span>
                      </div>
                      <div class="col-md-11">
                        <div class="row">
                          <span class="text-muted px-3">
                            {{
                              timeAgo(item.created_at) === "0 seconds"
                                ? "Just now"
                                : timeAgo(item.created_at) + " ago"
                            }}
                          </span>
                        </div>
                        <div class="row">
                          <span class="px-3"> {{ item.comment }}</span>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div
              :class="`col-md-${
                userdata.role === 'supervisor' ? 5 : 0
              } bg-light p-0`"
              v-show="userdata.role === 'supervisor'"
            >
              <div id="accordion">
                <div class="card">
                  <div class="card-header" id="headingOne">
                    <h5 class="mb-0 d-flex justify-content-between">
                      <span style="font-size: large">
                        <i class="fa fa-calendar"></i> {{ scheduleLabel }}
                      </span>
                      <span>
                        <i class="fas fa-chevron-down"></i>
                      </span>
                    </h5>
                  </div>
                  <div
                    id="collapseOne"
                    class="collapse show"
                    aria-labelledby="headingOne"
                    data-parent="#accordion"
                  >
                    <div class="card-body">
                      <div class="form-group row">
                        <label for="startdate" class="col-sm-4 col-form-label"
                          >Start Date:</label
                        >
                        <div class="col-sm-8">
                          <input
                            type="date"
                            :readonly="userdata.role !== 'supervisor'"
                            :disabled="task.isCompleted"
                            id="startdate"
                            class="form-control"
                            v-model="task.startDate"
                            @change="
                              updateTasks(
                                'changed startdate to ' + task.startDate
                              )
                            "
                          />
                        </div>
                      </div>
                      <div class="form-group row">
                        <label for="enddate" class="col-sm-4 col-form-label"
                          >End Date:</label
                        >
                        <div class="col-sm-8">
                          <input
                            type="date"
                            :readonly="userdata.role !== 'supervisor'"
                            :disabled="task.isCompleted"
                            id="enddate"
                            class="form-control"
                            v-model="task.endDate"
                            @change="
                              updateTasks('changed enddate to ' + task.endDate)
                            "
                          />
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
                <div class="card">
                  <div class="card-body">
                    <ul class="list-group list-group-flush">
                      <li class="list-group-item p-0">
                        <div class="row">
                          <div class="col-md-1">
                            <i class="fa fa-briefcase" aria-hidden="true"></i>
                          </div>
                          <div class="col-md-9">
                            <span style="font-weight: bold">Department</span>
                            <br />
                            <span v-if="!task.dept.isEditing" id="dept">{{
                              task.dept.name
                            }}</span>
                            <select
                              :disabled="task.isCompleted"
                              class="form-control form-control-sm mb-2"
                              v-else
                              v-model="task.dept.name"
                              @change="
                                updateTasks(
                                  'changed department to ' + task.dept.name
                                );
                                task.dept.isEditing = false;
                              "
                            >
                              <option value="">-- Department --</option>
                              <option value="Beach">Beach</option>
                              <option value="Office">Front Office</option>
                              <option value="Resto">Resto</option>
                              <option value="Pools">Pools</option>
                              <option value="Maintenance">
                                Maintenance/Engineering
                              </option>
                              <option value="Security">Security</option>
                              <option value="Housekeeping">Housekeeping</option>
                              <!-- Other options here -->
                            </select>
                          </div>

                          <div
                            class="col-md-2"
                            v-if="userdata.role === 'supervisor'"
                          >
                            <i
                              v-if="!task.dept.isEditing"
                              @click="task.dept.isEditing = true"
                              class="fas fa-pen text-primary"
                              aria-hidden="true"
                            ></i>
                            <i
                              v-else
                              @click="task.dept.isEditing = false"
                              class="fa fa-save text-primary"
                              aria-hidden="true"
                            ></i>
                          </div>
                        </div>
                      </li>

                      <li class="list-group-item p-0">
                        <div class="row">
                          <div class="col-md-1">
                            <i class="fa fa-briefcase" aria-hidden="true"></i>
                          </div>
                          <div class="col-md-9">
                            <span style="font-weight: bold">Status</span>
                            <br />
                            <span v-if="!task.status.isEditing" id="dept">{{
                              task.status.name
                            }}</span>
                            <select
                              :disabled="task.isCompleted"
                              class="form-control form-control-sm mb-2"
                              v-else
                              v-model="task.status.name"
                              @change="
                                updateTasks(
                                  'changed status to ' + task.status.name
                                );
                                task.status.isEditing = false;
                              "
                            >
                              <option value="Open">Open</option>
                              <option value="In progress">In progress</option>
                              <option value="Inspected">Inspected</option>
                              <!-- Other options here -->
                            </select>
                          </div>

                          <div
                            class="col-md-2"
                            v-if="userdata.role === 'supervisor'"
                          >
                            <i
                              v-if="!task.status.isEditing"
                              @click="task.status.isEditing = true"
                              class="fas fa-pen text-primary"
                              aria-hidden="true"
                            ></i>
                            <i
                              v-else
                              @click="task.status.isEditing = false"
                              class="fa fa-save text-primary"
                              aria-hidden="true"
                            ></i>
                          </div>
                        </div>
                      </li>

                      <li class="list-group-item p-0">
                        <div class="row">
                          <div class="col-md-1">
                            <i class="fas fa-plus-circle"></i>
                          </div>
                          <div class="col-md-11">
                            <span style="font-weight: bold">Created</span>
                            <br />
                            {{ task.created_at }}
                          </div>
                        </div>
                      </li>
                      <li class="list-group-item p-0">
                        <div class="row">
                          <div class="col-md-1">
                            <i class="fas fa-pen"></i>
                          </div>
                          <div class="col-md-11">
                            <span style="font-weight: bold">Updated</span>
                            <br />
                            {{ task.modified_at }}
                          </div>
                        </div>
                      </li>
                      <li class="list-group-item p-0">
                        <div class="row">
                          <div class="col-md-1">
                            <i class="fas fa-link"></i>
                          </div>
                          <div class="col-md-11">
                            <span style="font-weight: bold">Task ID</span><br />
                            {{ task.itemID }}
                          </div>
                        </div>
                      </li>
                    </ul>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <div
    class="modal fade"
    id="addTaskModal"
    tabindex="-1"
    aria-labelledby="addTaskModalLabel"
    aria-hidden="true"
  >
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="addTaskModalLabel">Add Task</h5>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
          ></button>
        </div>
        <div class="modal-body">
          <form @submit.prevent="loadNewTask">
            <div class="form-group row">
              <div class="col-sm-12">
                <input
                  type="text"
                  class="form-control"
                  v-model="task.name"
                  maxlength="64"
                  required
                  autocomplete="off"
                />
              </div>
            </div>
            <div class="form-group row mt-2">
              <div class="col-sm-6">
                <select class="form-control" v-model="task.dept.name" required>
                  <option value="">-- Department --</option>
                  <option value="Beach">Beach</option>
                  <option value="Office">Front Office</option>
                  <option value="Resto">Resto</option>
                  <option value="Pools">Pools</option>
                  <option value="Maintenance">Maintenance/Engineering</option>
                  <option value="Security">Security</option>
                  <option value="Housekeeping">Housekeeping</option>
                </select>
              </div>
              <div class="col-sm-6">
                <select
                  class="form-control"
                  id="clientType"
                  v-model="task.status.name"
                  required
                >
                  <option value="">-- Status --</option>
                  <option value="Open">Open</option>
                  <option value="In progress">In progress</option>
                  <option value="Inspected">Inspected</option>
                </select>
              </div>
            </div>
            <div class="form-group row mt-2">
              <div class="col-sm-12 d-flex flex-row-reverse">
                <button type="submit" class="btn btn-primary">
                  Create Task
                </button>
              </div>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { useAuthStore } from "@/stores/authStore";
import "/node_modules/vue-simple-calendar/dist/style.css";
import "/node_modules/vue-simple-calendar/dist/css/default.css";
import "/node_modules/vue-simple-calendar/dist/css/holidays-us.css";
import "/node_modules/vue-final-modal/dist/style.css";
import {
  CalendarView,
  CalendarViewHeader,
  CalendarMath,
} from "vue-simple-calendar";

function formatDate(date) {
  const yyyy = date.getFullYear();
  let mm = date.getMonth() + 1; // Months are 0-based, so +1
  let dd = date.getDate();

  // Convert month and date to 2 digits
  mm = (mm < 10 ? "0" : "") + mm;
  dd = (dd < 10 ? "0" : "") + dd;

  return yyyy + "-" + mm + "-" + dd;
}

export default {
  components: {
    CalendarView,
    CalendarViewHeader,
  },
  data() {
    return {
      //generic config for vue-simple-calendar
      showDate: this.thisMonth(1),
      message: "",
      socket: null,
      componentKey: 0,
      startingDayOfWeek: 1,
      disablePast: false,
      disableFuture: false,
      displayPeriodUom: "week",
      displayPeriodCount: 1,
      displayWeekNumbers: false,
      showTimes: true,
      selectionStart: null,
      selectionEnd: null,
      newItemTitle: "",
      newItemStartDate: "",
      newItemEndDate: "",
      useDefaultTheme: true,
      useHolidayTheme: true,
      useTodayIcons: false,
      //custom arrays
      tasks: [],
      temptasks: [],
      calendarItems: [
        // {
        //     // id: 'asasasasas',
        //     // startDate: new Date(),
        //     // endDate: new Date(),
        //     // title: 'asasasas',
        //     // classes: "purple",
        //     // tooltip: "This spans multiple days hehe",
        // },
      ],
      taskMembers: [],
      //custom configs
      dayreserve: new Date(),
      task: {
        itemID: "",
        name: "",
        dept: {
          name: "",
          isEditing: false,
        },
        status: {
          name: "",
          isEditing: false,
        },
        assign: {
          person: {
            name: "Staff",
            role: "",
          },
        },
        isNewMessage: false,
        isNotify: false,
        isCompleted: false,
        completionDate: "",
        states: [],
        actualStartTime: new Date().toLocaleTimeString(),
        startDate: formatDate(new Date()),
        endDate: formatDate(new Date()),
        desc: "",
        created_at: "",
        modified_at: "",
      },
      currentItemID: "",
      taskComment: "",
      assignedMember: "",
      isDropdownVisible: false,
      itemIndex: -1,
      isToggleTimeline: false,
      isToggleBox: false,
      itemDragged: null,
      dragSource: "",
      searchText: "",
      statusOrder: {
        Open: 0,
        "In progress": 1,
        Inspected: 2,
      },
    };
  },
  computed: {
    userdata() {
      const authStore = useAuthStore();
      const user = authStore.user;
      return user;
    },
    calcMeasure() {
      return {
        w1: parseFloat(window.innerWidth) - 300 + "px",
        h1: parseFloat(window.innerHeight) - 130 + "px",
      };
    },
    todayTasks() {
      const currentDate = new Date().setHours(0, 0, 0, 0);
      return this.tasks
        .filter((o) =>
          (o.taskname + o.dept + o.status + o.person_name)
            .toLowerCase()
            .includes(this.searchText.toLowerCase())
        )
        .filter((task) => {
          return (
            currentDate >= new Date(task.startDate).setHours(0, 0, 0, 0) &&
            currentDate <= new Date(task.endDate).setHours(0, 0, 0, 0)
          );
        })
        .sort((a, b) => {
          // Sort by isNotify
          if (b.isNotify !== a.isNotify) {
            return b.isNotify - a.isNotify;
          }

          // If person_name is also same, sort by status
          return this.statusOrder[a.status] - this.statusOrder[b.status];

          // If isNotify is same, sort by person_name
          if (a.person_name.toLowerCase() !== b.person_name.toLowerCase()) {
            return a.person_name.toLowerCase() < b.person_name.toLowerCase()
              ? -1
              : 1;
          }
        });
    },
    aggregateByPerson() {
      const result = this.todayTasks
        .filter((o) => !o.isCompleted)
        .reduce((acc, task) => {
          const o = acc.find((p) => p.person_name === task.person_name);
          const data = { ...task };
          delete data.person_name;
          if (o) {
            o.data.push(data);
          } else {
            acc.push({ person_name: task.person_name, data: [data] });
          }

          return acc;
        }, []);
      return result;
    },
    aggregateByDept() {
      const result = this.todayTasks
        .filter((o) => !o.isCompleted)
        .reduce((acc, task) => {
          const o = acc.find((p) => p.dept === task.dept);
          const data = { ...task };
          delete data.dept;
          if (o) {
            o.data.push(data);
          } else {
            acc.push({ dept: task.dept, data: [data] });
          }

          return acc;
        }, []);
      return result;
    },
    aggregateByStatus() {
      const result = this.todayTasks
        .filter((o) => !o.isCompleted)
        .reduce((acc, task) => {
          const o = acc.find((p) => p.status === task.status);
          const data = { ...task };
          delete data.status;
          if (o) {
            o.data.push(data);
          } else {
            acc.push({ status: task.status, data: [data] });
          }

          return acc;
        }, []);
      return result;
    },
    sortedStates() {
      return this.task.states.sort((a, b) => {
        const dateA = new Date(a.created_at);
        const dateB = new Date(b.created_at);
        return dateB - dateA;
      });
    },
    scheduleLabel() {
      if (this.task.startDate && this.task.endDate) {
        return `Scheduled for ${this.task.startDate} to ${this.task.endDate}`;
      } else {
        return "Not Scheduled";
      }
    },
    userLocale() {
      return CalendarMath.getDefaultBrowserLocale;
    },
    dayNames() {
      return CalendarMath.getFormattedWeekdayNames(this.userLocale, "long", 0);
    },
    themeClasses() {
      return {
        "theme-default": this.useDefaultTheme,
        "holiday-us-traditional": this.useHolidayTheme,
        "holiday-us-official": this.useHolidayTheme,
      };
    },
    myDateClasses() {
      // This was added to demonstrate the dateClasses prop. Note in particular that the
      // keys of the object are `yyyy-mm-dd` ISO date strings (not dates), and the values
      // for those keys are strings or string arrays. Keep in mind that your CSS to style these
      // may need to be fairly specific to make it override your theme's styles. See the
      // CSS at the bottom of this component to see how these are styled.
      const o = {};
      const theFirst = this.thisMonth(1);
      const ides = [2, 4, 6, 9].includes(theFirst.getMonth()) ? 15 : 13;
      const idesDate = this.thisMonth(ides);
      o[CalendarMath.isoYearMonthDay(idesDate)] = "ides";
      o[CalendarMath.isoYearMonthDay(this.thisMonth(21))] = [
        "do-you-remember",
        "the-21st",
      ];
      return o;
    },
    countBackLogTasks() {
      const today = new Date();
      today.setHours(0, 0, 0, 0);
      const count = this.tasks.filter((task) => {
        const taskDate = new Date(task.startDate);
        return !task.isCompleted && taskDate < today;
      }).length;
      return count;
    },
    currentDate() {
      const options = {
        month: "2-digit",
        day: "2-digit",
        year: "numeric",
        hour: "2-digit",
        minute: "2-digit",
        second: "2-digit",
        hour12: true,
      };
      return new Date().toLocaleString("en-US", options);
    },
  },
  async created() {
    this.loadData();
  },
  methods: {
    async loadData() {
      const response1 = await axios.get(this.API_URL + "task/");
      this.tasks = response1.data;
      const response2 = await axios.get(this.API_URL + "users/");
      this.taskMembers = response2.data.filter(
        (item) => item.role === "errand"
      );

      if (this.currentItemID !== "") {
        const newitem = this.tasks.filter(
          (o) => o.itemID === this.currentItemID
        )[0];
        const newid = newitem.itemID;
        this.setCommentData({ id: newid });
      }

      this.populateCalendarItems();
    },
    toggleNotify() {
      this.switchNotify();
      this.saveAction();
    },
    switchNotify() {
      this.task.isNotify = !this.task.isNotify;
      this.addComment(
        this.currentItemID,
        this.task.isNotify ? this.task.assign.person.name : this.userdata.role,
        `${
          this.task.isNotify ? "notified supervisor" : "saw your notification"
        }`
      );
    },
    moveTasktoNewday() {
      if (this.countBackLogTasks === 0) {
        return;
      }

      // Get today's date in 'YYYY-MM-DD' format and set time to midnight
      const today = new Date();
      today.setHours(0, 0, 0, 0);
      const formattedToday = formatDate(today);

      this.temptasks = JSON.parse(JSON.stringify(this.tasks));

      this.tasks = this.tasks.map((task) => {
        const taskDate = new Date(task.startDate);
        taskDate.setHours(0, 0, 0, 0);

        if (!task.isCompleted && taskDate < today) {
          const daysDifference = (today - taskDate) / (1000 * 60 * 60 * 24); // Calculate the difference in days

          const endDate = new Date(task.endDate);
          endDate.setDate(endDate.getDate() + daysDifference); // Shift the endDate by the same difference

          return {
            ...task,
            startDate: formattedToday, // Set startDate to today
            endDate: formatDate(endDate), // Use the shifted endDate
          };
        }
        return task;
      });

      this.populateCalendarItems();
      this.batchSaveAction();
    },

    async batchSaveAction() {
      const today = new Date();
      today.setHours(0, 0, 0, 0);
      const tasks = this.temptasks.filter((task) => {
        const taskDate = new Date(task.startDate);
        taskDate.setHours(0, 0, 0, 0);
        return !task.isCompleted && taskDate < today;
      });
      for (const item of tasks) {
        const formattedToday = formatDate(today);
        const taskDate = new Date(item.startDate);
        taskDate.setHours(0, 0, 0, 0);
        const daysDifference = (today - taskDate) / (1000 * 60 * 60 * 24);

        const endDate = new Date(item.endDate);
        endDate.setDate(endDate.getDate() + daysDifference); // Shift the endDate by the same difference

        const newstates = JSON.parse(item.states);
        newstates.push({
          created_at: new Date(),
          actor: this.userdata.role,
          comment: "changed startdate to " + formattedToday,
        });

        let data = {
          taskname: item.taskname,
          actualStartTime: item.actualStartTime,
          startDate: formattedToday,
          endDate: formatDate(endDate),
          person_name: item.person_name,
          person_role: item.person_role,
          dept: item.dept,
          taskdesc: item.taskdesc,
          status: item.status,
          itemID: item.itemID,
          isNewMessage: item.isNewMessage,
          isNotify: item.isNotify,
          isCompleted: item.isCompleted,
          completionDate: item.completionDate,
          processedBy: this.userdata.fName + " " + this.userdata.lName,
          groupkey: "",
          states: JSON.stringify(newstates),
        };
        await axios.put(`${this.API_URL}task/${item.id}/`, data);
      }
      this.taskRecord(`action:/moveTasktoNewday`);
      this.temptasks = [];
    },
    handleDragstart(e, o, source) {
      if (this.userdata.role !== "supervisor") {
        return;
      }
      this.itemDragged = o;
      this.dragSource = source;
    },
    handleDragdrop(e, prop, source) {
      e.preventDefault();
      if (this.userdata.role !== "supervisor") {
        return;
      }
      const data = this.itemDragged;
      if (data.isCompleted) {
        return;
      }
      this.task = {
        itemID: data.itemID,
        name: data.taskname,
        dept: {
          name:
            this.dragSource === source && source === "task"
              ? prop.dept
              : data.dept,
          isEditing: false,
        },
        status: {
          name:
            this.dragSource === source && source === "status"
              ? prop.status
              : data.status,
          isEditing: false,
        },
        assign: {
          person: {
            name:
              this.dragSource === source && source === "person"
                ? prop.person_name
                : data.person_name,
            role: data.person_role,
          },
        },
        isNewMessage: data.isNewMessage,
        isNotify: data.isNotify,
        isCompleted: data.isCompleted,
        completionDate: data.completionDate,
        states: JSON.parse(data.states),
        actualStartTime: data.actualStartTime,
        startDate: data.startDate,
        endDate: data.endDate,
        desc: data.taskdesc,
      };
      this.currentItemID = data.itemID;
      this.saveAction();
    },
    handleDragover(e) {
      e.preventDefault();
    },
    toggleTimeline() {
      this.isToggleTimeline = !this.isToggleTimeline;
      if (this.isToggleTimeline) {
        $(".calendar-parent").hide(1000);
        $(".c-h").animate({ height: this.calcMeasure.h1 });
      } else {
        $(".c-h").animate({ height: "335" });
        $(".calendar-parent").show(1000);
        $(".task-box").show(1000);
        $(".person-box").show(1000);
        $(".status-box").show(1000);
      }
    },
    toggleBox() {
      this.isToggleBox = !this.isToggleBox;
      if (this.isToggleBox) {
        $(".c-p").animate({ height: this.calcMeasure.h1 });
        $(".task-box").hide(1000);
        $(".person-box").hide(1000);
        $(".status-box").hide(1000);
      } else {
        $(".c-p").animate({ height: "400" });
        $(".task-box").show(1000);
        $(".person-box").show(1000);
        $(".status-box").show(1000);
      }
    },
    togglePersonBox() {
      $(".person-box").show(1000);
      $(".task-box").hide(1000);
      $(".status-box").hide(1000);
    },
    toggleTaskBox() {
      $(".person-box").hide(1000);
      $(".task-box").show(1000);
      $(".status-box").hide(1000);
    },
    toggleStatusBox() {
      $(".status-box").show(1000);
      $(".person-box").hide(1000);
      $(".task-box").hide(1000);
    },
    timeDiff(after, before) {
      const diffInSeconds = Math.floor(
        (new Date(after) -
          new Date(
            new Date(before).toLocaleDateString() +
              ", " +
              this.task.actualStartTime
          )) /
          1000
      );

      if (diffInSeconds < 60) {
        return `${diffInSeconds} seconds`;
      }

      const diffInMinutes = Math.floor(diffInSeconds / 60);
      if (diffInMinutes < 60) {
        return `${diffInMinutes} minutes`;
      }

      const diffInHours = Math.floor(diffInMinutes / 60);
      if (diffInHours < 24) {
        return `${diffInHours} hours`;
      }

      const diffInDays = Math.floor(diffInHours / 24);
      return `${diffInDays} days`;
    },
    timeAgo(dateString) {
      const now = Date.now();
      const date = new Date(dateString);
      const diffInSeconds = Math.floor((now - date) / 1000);

      if (diffInSeconds < 60) {
        return `${diffInSeconds} seconds`;
      }

      const diffInMinutes = Math.floor(diffInSeconds / 60);
      if (diffInMinutes < 60) {
        return `${diffInMinutes} minutes`;
      }

      const diffInHours = Math.floor(diffInMinutes / 60);
      if (diffInHours < 24) {
        return `${diffInHours} hours`;
      }

      const diffInDays = Math.floor(diffInHours / 24);
      return `${diffInDays} days`;
    },
    newComment(id, actor, comment) {
      this.addComment(id, actor, comment);
      this.task.isNewMessage = true;
      this.saveAction();
    },
    addComment(id, actor, comment) {
      this.generateArrayID(id);
      const data = this.tasks[this.itemIndex];
      const states = JSON.parse(data.states);
      const item = {
        created_at: new Date(),
        actor: actor,
        comment: comment,
      };
      states.push(item);
      this.task.states.push(item);
      data.states = JSON.stringify(this.task.states);
      this.taskComment = "";
    },
    completeTask() {
      this.task.isCompleted = !this.task.isCompleted;
      this.task.completionDate = this.task.isCompleted
        ? new Date().toLocaleString()
        : "";
      this.addComment(
        this.currentItemID,
        this.task.isCompleted
          ? this.task.assign.person.name
          : this.userdata.role,
        `${this.task.isCompleted ? "completed" : "restored"} the task on ${
          this.task.isCompleted
            ? this.task.completionDate
            : new Date().toLocaleString()
        }`
      );
      this.saveAction();
    },
    updateTasks(remarks) {
      this.addComment(this.currentItemID, this.userdata.role, remarks);
      this.task.isNewMessage = true;
      this.saveAction();
    },
    saveTaskChanges() {
      this.toggleModal("loadTaskModal");
      this.saveAction();
    },
    duplicateItem() {
      this.task.itemID =
        "t" + new Date().getTime().toString() + this.generateUniqueString();
      this.saveAction();
      this.toggleModal("loadTaskModal");
    },
    deleteItem() {
      this.$swal({
        title: "Are you sure?",
        text: "You won't be able to revert this!",
        icon: "warning",
        showCancelButton: true,
        confirmButtonText: "Yes, delete it!",
        cancelButtonText: "No, cancel!",
        reverseButtons: true,
      }).then((result) => {
        if (result.isConfirmed) {
          this.tasks = this.tasks.filter(
            (item) => item.itemID !== this.currentItemID
          );
          this.populateCalendarItems();

          axios.get(this.API_URL + "task/").then((response) => {
            this.temptasks = response.data;
            const itemTobedeleted = this.temptasks.filter(
              (o) => o.itemID === this.currentItemID
            );
            if (itemTobedeleted.length > 0) {
              axios
                .get(this.API_URL + `task/delete/${itemTobedeleted[0].id}/`)
                .then((response) => {
                  this.toggleModal("loadTaskModal");
                  this.$swal(
                    "Deleted!",
                    "Your item has been deleted.",
                    "success"
                  );
                });
            }
          });
        }
      });
    },
    checkLastMessage(e) {
      const states = JSON.parse(e.states);
      const lastMessage = states[states.length - 1];
      const actor = lastMessage.actor;
      if (actor !== this.userdata.role) {
        return true;
      }
      return false;
    },
    async saveAction() {
      let data = {
        taskname: this.task.name,
        actualStartTime: this.task.actualStartTime,
        startDate: this.task.startDate,
        endDate: this.task.endDate,
        person_name: this.task.assign.person.name || "Staff",
        person_role: this.task.assign.person.role || "Staff",
        dept: this.task.dept.name,
        taskdesc: this.task.desc,
        status: this.task.status.name,
        itemID: this.task.itemID,
        isNewMessage: this.task.isNewMessage,
        isNotify: this.task.isNotify,
        isCompleted: this.task.isCompleted,
        completionDate: this.task.completionDate,
        processedBy: this.userdata.fName + " " + this.userdata.lName,
        groupkey: "",
        states: JSON.stringify(this.task.states),
      };
      await axios.get(this.API_URL + "task/").then(async (response) => {
        const oldtask = this.tasks;
        this.tasks = response.data;
        const isDataExists =
          this.tasks.findIndex((o) => o.itemID === data.itemID) !== -1;
        if (!isDataExists) {
          this.tasks.push(data);

          // Make a POST request to the API to save the data
          await axios
            .post(this.API_URL + "task/", data)
            .then((response) => {
              // Log a success message to the console
            })
            .catch((error) => {
              // Log an error message to the console
              console.error("Error saving data:", error);
            });
          this.taskRecord(`action:/saveNewTask`);
        } else {
          this.generateArrayID(this.currentItemID);
          let item = this.tasks[this.itemIndex];
          item.taskname = data.taskname;
          item.actualStartTime = data.actualStartTime;
          item.startDate = data.startDate;
          item.endDate = data.endDate;
          item.person_name = data.person_name;
          item.persom_role = data.person_role;
          item.dept = data.dept;
          item.taskdesc = data.taskdesc;
          item.status = data.status;
          item.states = data.states;
          item.isNewMessage = data.isNewMessage;
          item.isNotify = data.isNotify;
          item.isCompleted = data.isCompleted;
          item.completionDate = data.completionDate;

          await axios.put(`${this.API_URL}task/${item.id}/`, data);

          this.taskRecord(`action:/updateTask`);
        }

        this.populateCalendarItems();
      });
    },
    onBoxItemClick(o) {
      const e = {
        id: o.itemID,
        startDate: o.startDate,
        endDate: o.endDate,
      };
      this.onClickItem(e);
    },
    onClickItem(e) {
      this.setInitialData(e);
      this.toggleNewMessage(e);
      this.toggleModal("loadTaskModal");
    },
    toggleNewMessage() {
      this.task.isNewMessage = false;
      this.saveAction();
    },
    setCommentData(e) {
      const data = this.tasks.filter((o) => o.itemID === e.id)[0];
      this.task.states = JSON.parse(data.states);
    },
    setInitialData(e) {
      this.currentItemID = e.id;
      this.generateArrayID(this.currentItemID);
      const data = this.tasks[this.itemIndex];
      this.task = {
        itemID: data.itemID,
        name: data.taskname,
        dept: {
          name: data.dept,
          isEditing: false,
        },
        status: {
          name: data.status,
          isEditing: false,
        },
        assign: {
          person: {
            name: data.person_name,
            role: data.person_role,
          },
        },
        isNewMessage: data.isNewMessage,
        isNotify: data.isNotify,
        isCompleted: data.isCompleted,
        completionDate: data.completionDate,
        states: JSON.parse(data.states),
        actualStartTime: data.actualStartTime,
        startDate: data.startDate,
        endDate: data.endDate,
        desc: data.taskdesc,
        created_at: new Date(data.created_at).toLocaleString(),
        modified_at: new Date(data.modified_at).toLocaleString(),
      };
    },
    generateArrayID(ref) {
      this.itemIndex = this.tasks.findIndex((o) => o.itemID === ref);
    },
    generateUniqueString() {
      let randomString = "";
      while (randomString.length < 8) {
        randomString += Math.random().toString(36).substr(2, 36);
      }
      randomString = randomString.substr(0, 8);
      return randomString;
    },
    toggleDropdown() {
      this.isDropdownVisible = !this.isDropdownVisible;
    },
    addNewTask() {
      this.task.name = "";
      this.task.dept = {
        name: "",
        isEditing: false,
      };
      this.task.status = {
        name: "",
        isEditing: false,
      };
      this.task.assign = {
        person: {
          name: "Staff",
          role: "",
        },
      };
      this.task.completionDate = "";
      this.task.desc = "";
      this.task.created_at = new Date().toLocaleString();
      this.task.modified_at = new Date().toLocaleString();
      this.taskComment = "";

      this.toggleModal("addTaskModal");
    },
    loadNewTask() {
      this.toggleModal("addTaskModal");
      this.toggleModal("loadTaskModal");
      let id =
        "t" + new Date().getTime().toString() + this.generateUniqueString();
      this.task.itemID = id;
      this.currentItemID = id;
      this.task.isNewMessage = false;
      this.task.isCompleted = false;
      this.task.isNotify = false;
      this.task.actualStartTime = new Date().toLocaleTimeString();
      this.task.states = [
        {
          created_at: new Date(),
          actor: this.userdata.role,
          comment: "created the task on " + new Date().toLocaleString(),
        },
      ];
      this.saveAction();
    },
    thisMonth(d, h, m) {
      const t = new Date();
      return new Date(t.getFullYear(), t.getMonth(), d, h || 0, m || 0);
    },
    periodChanged() {
      // range, eventSource) {
      // Demo does nothing with this information, just including the method to demonstrate how
      // you can listen for changes to the displayed range and react to them (by loading items, etc.)
      //console.log(eventSource)
      //console.log(range)
    },
    setShowDate(d) {
      this.showDate = d;
    },
    onClickDay(d) {
      if (this.userdata.role !== "supervisor") {
        return;
      }
      this.dayreserve = d;
      this.task.startDate = formatDate(this.dayreserve);
      this.task.endDate = formatDate(this.dayreserve);
      this.addNewTask();
    },
    setSelection(dateRange) {
      if (this.userdata.role !== "supervisor") {
        return;
      }
      this.selectionEnd = dateRange[1];
      this.selectionStart = dateRange[0];
    },
    finishSelection(dateRange) {
      if (this.userdata.role !== "supervisor") {
        return;
      }
      this.task.startDate = formatDate(dateRange[0]);
      this.task.endDate = formatDate(dateRange[1]);
      this.addNewTask();
    },
    onDrop(item, date) {
      if (this.userdata.role !== "supervisor") {
        return;
      }
      this.setInitialData(item);
      const data = this.tasks[this.itemIndex];
      if (data.isCompleted) {
        return;
      }
      const eLength = CalendarMath.dayDiff(item.startDate, date);
      if (event.ctrlKey) {
        let sd = CalendarMath.addDays(item.startDate, 0);
        let ed = CalendarMath.addDays(
          item.endDate,
          eLength - CalendarMath.dayDiff(item.startDate, item.endDate)
        );
        if (ed >= sd) {
          item.originalItem.startDate = sd;
          item.originalItem.endDate = ed;
          this.task.startDate = formatDate(sd);
          this.task.endDate = formatDate(ed);
        } else {
          item.originalItem.endDate = item.endDate;
          item.originalItem.startDate = ed;
          this.task.startDate = formatDate(ed);
          this.task.endDate = formatDate(item.endDate);
        }
      } else {
        item.originalItem.startDate = CalendarMath.addDays(
          item.startDate,
          eLength
        );
        item.originalItem.endDate = CalendarMath.addDays(item.endDate, eLength);
        this.task.startDate = formatDate(
          CalendarMath.addDays(item.startDate, eLength)
        );
        this.task.endDate = formatDate(
          CalendarMath.addDays(item.endDate, eLength)
        );
      }
      this.task.itemID = this.currentItemID;
      this.populateCalendarItems();
      this.addComment(
        this.currentItemID,
        this.userdata.role,
        "changed startdate to " + this.task.startDate
      );
      this.addComment(
        this.currentItemID,
        this.userdata.role,
        "changed enddate to " + this.task.endDate
      );
      this.saveAction();
    },
    toggleModal(id) {
      $(`#${id}`).modal("toggle");
    },
    populateCalendarItems() {
      this.calendarItems = this.tasks.map((task) => {
        const startDate = task.startDate;
        const endDate = task.endDate;
        const title = `${task.taskname}<span style="display:none">~${task.itemID}~</span>`;
        const id = task.itemID;
        const tooltip = "test";
        let classes = "";
        if (task.status === "Open") {
          classes = ["task-open"];
        } else if (task.status === "In progress") {
          classes = ["task-progress"];
        } else {
          classes = ["task-inspected"];
        }
        if (task.isCompleted) {
          classes = ["task-completed"];
        }
        return { startDate, endDate, title, id, classes, tooltip };
      });
    },
    async logOut() {
      const authStore = useAuthStore();
      const user = {
        username: authStore.user.username,
        FirstName: authStore.user.fName,
        LastName: authStore.user.lName,
        role: authStore.user.role,
        route: authStore.user.route,
      };
      const response = await axios.put(
        `${this.API_URL}users/${authStore.user.id}/`,
        { ...user, isActive: false }
      );
      if (response.data !== undefined) {
        authStore.logout();
        this.$router.push("/");
      } else {
        this.$swal({
          icon: "error",
          title: "Logout error. Please contact your admin for assistance!",
        });
      }
    },
    async taskRecord(msg) {
      this.socket.send(
        JSON.stringify({
          message: msg,
        })
      );
      try {
        await axios.post(`${this.API_URL}task/record/`, {
          actor: this.userdata.fName + " " + this.userdata.lName,
          task: msg,
        });
      } catch (error) {}
    },
  },
  mounted() {
    var vm = this;
    $(document).on("click", function (e) {
      // Check if the clicked element or its parents don't have the 'btn-dropdown' class
      if (
        !$(e.target).hasClass("btn-dropdown") &&
        $(e.target).closest(".btn-dropdown").length === 0
      ) {
        vm.isDropdownVisible = false;
      }
    });
    $(".currentPeriod").click();
    this.newItemStartDate = CalendarMath.isoYearMonthDay(CalendarMath.today());
    this.newItemEndDate = CalendarMath.isoYearMonthDay(CalendarMath.today());
    this.socket = new WebSocket(
      `ws://${this.API_URL.replace(/^https?:\/\//, "")}ws/realtime/`
    );
    this.socket.onmessage = function (e) {
      const data = JSON.parse(e.data);
      console.log(data.message);
      vm.loadData();
    };

    if (this.userdata.role !== "supervisor") {
      setTimeout(() => {
        this.toggleTimeline();
        this.toggleTaskBox();
      }, 1000);
    }
  },
};
</script>
<style scoped>
.calendar-parent {
  overflow-x: hidden;
  overflow-y: hidden;
  height: 400px;
  background-color: white;
}

.list-item {
  border-radius: 0.5em;
  border-color: #e0e0f0;
  text-overflow: ellipsis;
  box-shadow: 0 0.125rem 0.25rem rgba(0, 0, 0, 0.075);
  border: 1px solid #dee2e6;
  transition: all 0.2s ease-in-out;
  direction: initial;
  color: white;
  font-family:
    Avenir,
    Avenir Next,
    Segoe UI,
    Helvetica,
    Arial,
    sans-serif;
  font-size: medium;
}

.app-header {
  background-color: #3d474d;
  color: white;
  box-shadow: 0 0.125rem 0.5rem rgba(0, 0, 0, 0.2);
  padding-top: 10px;
  padding-bottom: 10px;
  padding-left: 5px;
  padding-right: 5px;
  margin: 0px;
}

.list-item:hover {
  cursor: pointer;
  transform: translateY(-5px);
  box-shadow: 0 0.5rem 1rem rgba(0, 0, 0, 0.15);
}

.task-progress {
  background-color: rgb(0, 170, 255);
  /* adjust the color as needed */
}

.task-inspected {
  background-color: rgb(46, 215, 216);
  /* adjust the color as needed */
}

.task-open {
  background-color: rgb(208, 31, 46);
  /* adjust the color as needed */
}

.task-completed {
  background-color: rgb(255, 170, 0);
  /* adjust the color as needed */
}

.task-incomplete {
  background-color: aliceblue;
  color: #3d474d;
  /* adjust the color as needed */
}

.btn-item {
  position: relative;
  white-space: nowrap;
  overflow: hidden;
  border-width: 1px;
  direction: initial;
  box-shadow: 0 0.125rem 0.25rem rgba(0, 0, 0, 0.075);
  border: 1px solid #f7fcff;
  border-radius: 1rem;
  transition: all 0.2s ease-in-out;
  text-align: center;
}

.btn-item:hover {
  cursor: pointer;
  transform: translateY(-5px);
  box-shadow: 0 0.5rem 1rem rgba(0, 0, 0, 0.15);
}

.btn-circle {
  border-radius: 50%;
  /* Makes the button circular */
  padding: 5px 10px;
  /* Adjust as per your need */
  background-color: #007bff;
  /* Default bootstrap primary color */
  color: #fff;
  /* White color for the icon */
}

.icon-container {
  align-items: center;
  /* Optional: to vertically center the icons if they are of different sizes */
}

.icon-wrapper {
  /* border-right: 2px solid rgb(23, 25, 26); */
  /* You can change the color as per your design */
  padding: 0 10px;
  /* This gives a little spacing around the icon, adjust values as needed */
}

.icon-wrapper:last-child {
  border-right: none;
  /* Removes border for the last icon */
}

/* CSS for the continuous wiggle animation */
@keyframes wiggle {
  0% {
    transform: rotate(0deg);
  }

  25% {
    transform: rotate(5deg);
  }

  50% {
    transform: rotate(-5deg);
  }

  75% {
    transform: rotate(5deg);
  }

  100% {
    transform: rotate(0deg);
  }
}

/* Apply the animation to the button */
.wiggle-animation {
  animation: wiggle 0.75s infinite;
  /* Adjust animation duration as needed */
}
.align-icon {
  float: right;
}

.list-txtdesc {
  width: 240px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
</style>
