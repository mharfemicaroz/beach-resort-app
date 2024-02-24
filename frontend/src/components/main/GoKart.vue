<template :key="componentKey">
  <div class="container-fluid mt-3">
    <div class="row app-header">
      <div class="col-md-12">
        <div class="d-flex justify-content-between">
          <div>
            <a
              class="navbar-brand text-dark align-middlev vv vv v vv v"
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
                  <span class="h4"><b>GoKart</b></span>
                  <a
                    href="#"
                    v-if="
                      userdata.role === 'supervisor' ||
                      userdata.role === 'superuser'
                    "
                    class="btn btn-link text-decoration-none text-white"
                    @click="toggleModal('settings-modal')"
                    data-bs-toggle="tooltip"
                    data-bs-placement="top"
                    title="Show settings"
                  >
                    <i class="fa fa-bars text-dark" style="font-size: 24px"></i>
                  </a>
                </div>
                <span
                  class="search-bar-container"
                  style="margin-right: 10px; display: flex; align-items: center"
                >
                  <input
                    v-model="searchText"
                    type="text"
                    class="form-control bg-dark text-white"
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
                v-if="
                  userdata.role === 'supervisor' ||
                  userdata.role === 'superuser'
                "
                class="btn btn-link text-decoration-none text-white"
                @click="addNewTask"
              >
                <i
                  class="fa fa-plus-circle text-dark"
                  style="font-size: 24px"
                ></i>
              </a>
              <a
                href="#"
                v-if="
                  countBookedKarts > 0 &&
                  (userdata.role === 'supervisor' ||
                    userdata.role === 'superuser')
                "
                class="btn btn-link text-decoration-none text-white"
                @click="changeKartStatus('Booked', 'Rented')"
              >
                <i
                  class="fas fa-play position-relative text-dark"
                  style="font-size: 24px"
                >
                  <span
                    class="badge bg-danger position-absolute top-0 start-100 translate-middle"
                    style="font-size: 12px; transform: translate(50%, -50%)"
                  >
                    {{ countBookedKarts }}
                  </span>
                </i>
              </a>
              <a
                href="#"
                v-if="
                  countRentedKarts > 0 &&
                  (userdata.role === 'supervisor' ||
                    userdata.role === 'superuser')
                "
                class="btn btn-link text-decoration-none text-white"
                @click="changeKartStatus('Rented', 'Returned')"
              >
                <i
                  class="fas fa-rotate-left position-relative text-dark"
                  style="font-size: 24px"
                >
                  <span
                    class="badge bg-danger position-absolute top-0 start-100 translate-middle"
                    style="font-size: 12px; transform: translate(50%, -50%)"
                  >
                    {{ countRentedKarts }}
                  </span>
                </i>
              </a>
            </div>
            <div>
              <a
                v-if="!isToggleBox"
                href="#"
                class="btn btn-link text-dark text-decoration-none timeline"
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
                class="btn btn-link text-dark text-decoration-none"
                @click="toggleTaskBox"
              >
                <i class="fa fa-car" style="font-size: 24px"></i>
              </a>
              <a
                href="#"
                class="btn btn-link text-dark text-decoration-none"
                @click="toggleStatusBox"
              >
                <i class="fas fa-check-circle" style="font-size: 24px"></i>
              </a>
            </div>
            <div class="icon-wrapper">
              <a
                href="#"
                v-if="!isToggleTimeline"
                class="btn btn-link text-dark text-decoration-none"
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
                class="btn btn-link text-dark text-decoration-none"
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
            v-for="(item, index) in aggregateByVehicle"
            :key="index"
          >
            <div class="card c-h" style="width: 200px; height: 335px">
              <div
                class="card-header bg-light text-dark d-flex justify-content-between"
              >
                <h4>
                  <i class="fa fa-car mr-3 p-0"></i>
                  {{ item.vehicle }}
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
                  width: 200px;
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
                          : itemData.status === 'Booked'
                          ? 'task-booked'
                          : itemData.status === 'Rented'
                          ? 'task-rented'
                          : itemData.status === 'Returned'
                          ? 'task-returned'
                          : ''
                      }`,
                    ]"
                    v-for="(itemData, index2) in item.data"
                    :key="index2"
                    @click="onBoxItemClick(itemData)"
                  >
                    <div class="d-flex justify-content-between">
                      <span class="list-txtdesc"
                        >{{ itemData.clientname }}
                      </span>
                      <span v-if="itemData.isPaid" class="p-0 m-0">
                        <i
                          class="fa fa-money-bill text-white"
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
            <div class="card c-h" style="width: 200px; height: 335px">
              <div
                class="card-header text-white d-flex justify-content-between"
                :class="[
                  `${
                    item.status === 'Booked'
                      ? 'task-booked'
                      : item.status === 'Rented'
                      ? 'task-rented'
                      : item.status === 'Returned'
                      ? 'task-returned'
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
                  width: 200px;
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
                      <span class="list-txtdesc">{{
                        itemData.clientname
                      }}</span>
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
                        Booked <i class="fas fa-calendar-check align-icon"></i>
                      </td>
                      <td class="task-booked"></td>
                    </tr>
                    <tr>
                      <td>Rented <i class="fas fa-tag align-icon"></i></td>
                      <td class="task-rented"></td>
                    </tr>
                    <tr>
                      <td>Returned <i class="fas fa-undo align-icon"></i></td>
                      <td class="task-returned"></td>
                    </tr>
                    <tr>
                      <td>
                        Completed <i class="fas fa-check-circle align-icon"></i>
                      </td>
                      <td class="task-completed"></td>
                    </tr>
                    <tr>
                      <td>
                        Incomplete
                        <i class="fas fa-times-circle align-icon"></i>
                      </td>
                      <td class="task-incomplete"></td>
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
        userdata.role === 'supervisor' || userdata.role === 'superuser'
          ? 'modal-lg'
          : ''
      }`"
    >
      <div class="modal-content p-3">
        <div class="modal-header">
          <div class="d-flex justify-content-between w-100">
            <div></div>
            <!-- <div class="d-flex align-items-center">
              <button
                type="button"
                @click="completeTask"
                v-if="
                  userdata.role === 'supervisor' ||
                  userdata.role === 'superuser'
                "
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
            </div> -->
            <div>
              <!-- Button that triggers the dropdown -->
              <button
                type="button"
                v-if="
                  userdata.role === 'supervisor' ||
                  userdata.role === 'superuser'
                "
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
                  <a
                    class="dropdown-item"
                    href="#"
                    @click="
                      toggleDropdown();
                      printInvoice();
                    "
                  >
                    <i class="fas fa-print"></i> Print Invoice
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
          </div>
          <div class="row">
            <div
              :class="`col-md-${
                userdata.role === 'supervisor' || userdata.role === 'superuser'
                  ? 7
                  : 12
              }`"
            >
              <div class="form-group row">
                <div class="col-sm-12">
                  <input
                    :disabled="task.isCompleted"
                    type="text"
                    placeholder="Add task name"
                    class="form-control"
                    style="font-size: x-large; border: 0"
                    v-model="task.clientname"
                    required
                    autocomplete="off"
                    @change="
                      updateTasks('changed task name to ' + task.clientname)
                    "
                  />
                </div>
              </div>
              <div class="form-group row mt-2">
                <div class="col-sm-12">
                  <textarea
                    :disabled="task.isCompleted"
                    placeholder="Add task description"
                    class="form-control"
                    style="font-size: medium; border: 0; color: darkgray"
                    v-model="task.desc"
                    required
                    @change="
                      updateTasks('changed task description to ' + task.desc)
                    "
                  ></textarea>
                </div>
              </div>
            </div>
            <div
              :class="`col-md-${
                userdata.role === 'supervisor' || userdata.role === 'superuser'
                  ? 5
                  : 0
              } bg-light p-0`"
              v-show="
                userdata.role === 'supervisor' || userdata.role === 'superuser'
              "
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
                            <i class="fa fa-car" aria-hidden="true"></i>
                          </div>
                          <div class="col-md-9">
                            <span style="font-weight: bold">Vehicle</span>
                            <br />
                            <span v-if="!task.vehicle.isEditing" id="dept">{{
                              task.vehicle.name
                            }}</span>
                            <select
                              :disabled="task.isCompleted"
                              class="form-control form-control-sm mb-2"
                              v-else
                              v-model="task.vehicle.name"
                              @change="
                                updateTasks(
                                  'changed department to ' + task.vehicle.name
                                );
                                task.vehicle.isEditing = false;
                              "
                            >
                              <option value="">-- Vehicle --</option>
                              <option
                                v-for="(item, index) in gokarts"
                                :key="index"
                                :value="item.name"
                              >
                                {{ item.name }}
                              </option>
                              <!-- Other options here -->
                            </select>
                          </div>

                          <div
                            class="col-md-2"
                            v-if="
                              !task.isCompleted &&
                              (userdata.role === 'supervisor' ||
                                userdata.role === 'superuser')
                            "
                          >
                            <i
                              v-if="!task.vehicle.isEditing"
                              @click="task.vehicle.isEditing = true"
                              class="fas fa-pen text-primary"
                              aria-hidden="true"
                            ></i>
                            <i
                              v-else
                              @click="task.vehicle.isEditing = false"
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
                              <option value="Booked">Booked</option>
                              <option value="Rented">Rented</option>
                              <option value="Returned">Returned</option>
                              <!-- Other options here -->
                            </select>
                          </div>

                          <div
                            class="col-md-2"
                            v-if="
                              countRentedKartsByOne < 1 &&
                              !task.isCompleted &&
                              (userdata.role === 'supervisor' ||
                                userdata.role === 'superuser')
                            "
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
          <h5 class="modal-title" id="addTaskModalLabel">Add Customer</h5>
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
                  v-model="task.clientname"
                  placeholder="Input customer's name"
                  maxlength="64"
                  required
                  autocomplete="off"
                />
              </div>
            </div>
            <div class="form-group row mt-2">
              <div class="col-sm-6">
                <select
                  class="form-control"
                  v-model="task.vehicle.name"
                  required
                >
                  <option value="">-- Vehicle --</option>
                  <option
                    v-for="(item, index) in gokarts"
                    :key="index"
                    :value="item.name"
                  >
                    {{ item.name }}
                  </option>
                </select>
              </div>
              <div class="col-sm-6">
                <select
                  class="form-control"
                  id="clientType"
                  v-model="task.status.name"
                  required
                >
                  <option value="Booked">Booked</option>
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

  <div
    class="modal modal_outer right_modal fade"
    id="invoiceModal"
    tabindex="-1"
    aria-labelledby="invoiceLabel"
    aria-hidden="true"
  >
    <div class="modal-dialog modal-lg">
      <div class="modal-content">
        <div class="modal-header">
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
          ></button>
        </div>
        <div class="modal-body">
          <in-voice
            :invoiceId="task.itemID"
            :actor="task.clientname"
            :desc="task.desc"
            :isPaid="task.isPaid"
            :invdata="invoiceData"
            @pay-action="payAction"
          />
        </div>
      </div>
    </div>
  </div>

  <div
    class="modal fade"
    id="payformModal"
    tabindex="-1"
    aria-labelledby="payformLabel"
    aria-hidden="true"
  >
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
          ></button>
        </div>
        <div class="modal-body">
          <payment-form :totalCost="totalCost" />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { useAuthStore } from "@/stores/authStore";
import inVoice from "@/components/common/inVoice.vue";
import paymentForm from "@/components/common/paymentForm.vue";
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
    inVoice,
    paymentForm,
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
        clientname: "",
        vehicle: {
          name: "",
          price: 0,
          isEditing: false,
        },
        status: {
          name: "Booked",
          isEditing: false,
        },
        isPaid: false,
        isCompleted: false,
        completionDate: "",
        actualStartTime: new Date().toLocaleTimeString(),
        startDate: formatDate(new Date()),
        endDate: formatDate(new Date()),
        desc: "",
        created_at: "",
        modified_at: "",
      },
      gokarts: [],
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
      totalCost: 0,
      statusOrder: {
        Booked: 0,
        Rented: 1,
        Returned: 2,
      },
    };
  },
  computed: {
    userdata() {
      const authStore = useAuthStore();
      const user = authStore.user;
      return user;
    },
    todayTasks() {
      const currentDate = new Date().setHours(0, 0, 0, 0);
      return this.tasks
        .filter((o) =>
          (o.taskname + o.vehicle + o.status)
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
          // If person_name is also same, sort by status
          return this.statusOrder[a.status] - this.statusOrder[b.status];
        });
    },
    vouchInvoice() {
      const filteredTasks = this.tasks.filter((item) => {
        const today = new Date().setHours(0, 0, 0, 0);
        const taskDate = new Date(item.startDate).setHours(0, 0, 0, 0);
        return (
          taskDate === today &&
          item.clientname === this.task.clientname &&
          item.isPaid === this.task.isPaid
        );
      });
      return filteredTasks;
    },
    invoiceData() {
      let filteredTasks = this.vouchInvoice;
      const mergedTasks = filteredTasks.reduce((accumulator, task) => {
        // If the vehicle is already in the accumulator, increase the quantity
        if (accumulator[task.vehicle]) {
          accumulator[task.vehicle].qty += 1;
          accumulator[task.vehicle].total =
            parseFloat(accumulator[task.vehicle].total) +
            parseFloat(task.duebal);
        } else {
          // Otherwise, add the new vehicle to the accumulator
          accumulator[task.vehicle] = {
            item: task.vehicle,
            qty: 1,
            price: task.duebal,
            total: task.duebal,
          };
        }
        return accumulator;
      }, {});

      // Convert the object back into an array of merged tasks
      return Object.values(mergedTasks);
    },
    countRentedKartsByOne() {
      const today = new Date().setHours(0, 0, 0, 0);
      const count = this.tasks.filter((task) => {
        const taskDate = new Date(task.startDate).setHours(0, 0, 0, 0);
        return (
          task.status === "Rented" &&
          (this.task.status.name === "Booked" ||
            this.task.status.name === "Returned") &&
          task.vehicle === this.task.vehicle.name &&
          !task.isCompleted &&
          taskDate === today
        );
      }).length;
      return count;
    },
    countBookedKarts() {
      const today = new Date().setHours(0, 0, 0, 0);
      const count = this.tasks.filter((task) => {
        const taskDate = new Date(task.startDate).setHours(0, 0, 0, 0);
        return (
          task.status === "Booked" && !task.isCompleted && taskDate === today
        );
      }).length;
      return count;
    },
    countRentedKarts() {
      const today = new Date().setHours(0, 0, 0, 0);
      const count = this.tasks.filter((task) => {
        const taskDate = new Date(task.startDate).setHours(0, 0, 0, 0);
        return (
          task.status === "Rented" && !task.isCompleted && taskDate === today
        );
      }).length;
      return count;
    },
    aggregateByVehicle() {
      const result = this.todayTasks
        .filter((o) => !o.isCompleted)
        .reduce((acc, task) => {
          const o = acc.find((p) => p.vehicle === task.vehicle);
          const data = { ...task };
          delete data.vehicle;
          if (o) {
            o.data.push(data);
          } else {
            acc.push({ vehicle: task.vehicle, data: [data] });
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
    calcMeasure() {
      return {
        w1: parseFloat(window.innerWidth) - 500 + "px",
        h1: parseFloat(window.innerHeight) - 130 + "px",
      };
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
    startBackgroundSlideshow() {
      setInterval(() => {
        this.backgroundIndex =
          (this.backgroundIndex + 1) % this.backgrounds.length;
      }, 5000);
    },
    toggleModal(id) {
      $(`#${id}`).modal("toggle");
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
        $(".status-box").hide(1000);
      } else {
        $(".c-p").animate({ height: "400" });
        $(".task-box").show(1000);
        $(".status-box").show(1000);
      }
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
    toggleDropdown() {
      this.isDropdownVisible = !this.isDropdownVisible;
    },
    changeKartStatus(oldstatus, newstatus) {
      const today = new Date().setHours(0, 0, 0, 0);
      const count = this.tasks.filter((task) => {
        const taskDate = new Date(task.startDate).setHours(0, 0, 0, 0);
        return (
          task.status === oldstatus && !task.isCompleted && taskDate === today
        );
      }).length;

      if (count === 0) {
        return;
      }
      this.temptasks = JSON.parse(JSON.stringify(this.tasks));

      this.tasks = this.tasks.map((task) => {
        const taskDate = new Date(task.startDate).setHours(0, 0, 0, 0);

        if (
          !task.isCompleted &&
          task.status === oldstatus &&
          taskDate === today
        ) {
          return {
            ...task,
            status: newstatus,
          };
        }
        return task;
      });

      this.populateCalendarItems();
      this.batchSaveAction(oldstatus, newstatus);
    },
    async batchSaveAction(oldstatus, newstatus) {
      const today = new Date().setHours(0, 0, 0, 0);
      const tasks = this.temptasks.filter((task) => {
        const taskDate = new Date(task.startDate).setHours(0, 0, 0, 0);
        return (
          !task.isCompleted && task.status === oldstatus && taskDate === today
        );
      });
      for (const item of tasks) {
        let data = {
          clientname: item.clientname,
          actualStartTime: item.actualStartTime,
          startDate: item.startDate,
          endDate: item.endDate,
          vehicle: item.vehicle,
          duebal: item.duebal,
          isPaid: item.isPaid,
          desc: item.desc,
          status: newstatus,
          itemID: item.itemID,
          isCompleted: item.isCompleted,
          completionDate: item.completionDate,
          processedBy: this.userdata.fName + " " + this.userdata.lName,
        };
        await axios.put(`${this.API_URL}gokart/${item.id}/`, data);
      }
      this.temptasks = [];
    },
    duplicateItem() {
      this.task.itemID =
        "t" + new Date().getTime().toString() + this.generateUniqueString();
      this.task.isPaid = false;
      this.task.isCompleted = false;
      this.task.completionDate = "";
      this.task.status.name = "Booked";
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

          axios.get(this.API_URL + "gokart/").then((response) => {
            this.temptasks = response.data;
            const itemTobedeleted = this.temptasks.filter(
              (o) => o.itemID === this.currentItemID
            );
            if (itemTobedeleted.length > 0) {
              axios
                .get(this.API_URL + `gokart/delete/${itemTobedeleted[0].id}/`)
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
    handleDragstart(e, o, source) {
      if (
        this.userdata.role !== "supervisor" &&
        this.userdata.role !== "superuser"
      ) {
        return;
      }
      this.itemDragged = o;
      this.dragSource = source;
    },
    handleDragdrop(e, prop, source) {
      e.preventDefault();
      if (
        this.userdata.role !== "supervisor" &&
        this.userdata.role !== "superuser"
      ) {
        return;
      }
      const data = this.itemDragged;
      if (data.isCompleted) {
        return;
      }
      this.task = {
        itemID: data.itemID,
        clientname: data.clientname,
        vehicle: {
          name:
            this.dragSource === source && source === "task"
              ? prop.vehicle
              : data.vehicle,
          price:
            this.dragSource === source && source === "task"
              ? prop.duebal
              : data.duebal,
          isEditing: false,
        },
        status: {
          name:
            this.dragSource === source && source === "status"
              ? prop.status
              : data.status,
          isEditing: false,
        },
        duebal: parseFloat(data.duebal),
        isPaid: data.isPaid,
        isCompleted: data.isCompleted,
        completionDate: data.completionDate,
        actualStartTime: data.actualStartTime,
        startDate: data.startDate,
        endDate: data.endDate,
        desc: data.desc,
      };
      this.currentItemID = data.itemID;
      this.saveAction();
    },
    handleDragover(e) {
      e.preventDefault();
    },
    onBoxItemClick(o) {
      const e = {
        id: o.itemID,
        startDate: o.startDate,
        endDate: o.endDate,
      };
      this.onClickItem(e);
    },
    printInvoice() {
      this.toggleModal("loadTaskModal");
      this.toggleModal("invoiceModal");
    },
    payAction(total) {
      this.totalCost = total;

      this.toggleModal("invoiceModal");

      setTimeout(() => {
        this.task.isCompleted = true;
        this.task.isPaid = true;
        this.batchPay();
        this.toggleModal("invoiceModal");
      }, 500);
    },
    async batchPay() {
      const today = new Date().setHours(0, 0, 0, 0);
      let data = this.tasks.filter((item) => {
        const taskDate = new Date(item.startDate).setHours(0, 0, 0, 0);
        return (
          taskDate === today &&
          item.clientname === this.task.clientname &&
          item.isPaid === !this.task.isPaid
        );
      });

      this.tasks = this.tasks.map((task) => {
        const taskDate = new Date(task.startDate).setHours(0, 0, 0, 0);

        if (
          task.isPaid === !this.task.isPaid &&
          task.clientname === this.task.clientname &&
          taskDate === today
        ) {
          return {
            ...task,
            isPaid: true,
            isCompleted: true,
            completionDate: new Date().toLocaleString(),
          };
        }
        return task;
      });

      this.populateCalendarItems();

      for (const item of data) {
        let data = {
          clientname: item.clientname,
          actualStartTime: item.actualStartTime,
          startDate: item.startDate,
          endDate: item.endDate,
          vehicle: item.vehicle,
          duebal: item.duebal,
          isPaid: true,
          desc: item.desc,
          status: item.status,
          itemID: item.itemID,
          isCompleted: true,
          completionDate: new Date().toLocaleString(),
          processedBy: this.userdata.fName + " " + this.userdata.lName,
        };
        await axios.put(`${this.API_URL}gokart/${item.id}/`, data);
      }
    },
    setInitialData(e) {
      this.currentItemID = e.id;
      this.generateArrayID(this.currentItemID);
      const data = this.tasks[this.itemIndex];
      this.task = {
        itemID: data.itemID,
        clientname: data.clientname,
        vehicle: {
          name: data.vehicle,
          price: data.duebal,
          isEditing: false,
        },
        status: {
          name: data.status,
          isEditing: false,
        },
        isPaid: data.isPaid,
        isCompleted: data.isCompleted,
        completionDate: data.completionDate,
        actualStartTime: data.actualStartTime,
        startDate: data.startDate,
        endDate: data.endDate,
        desc: data.desc,
        created_at: new Date(data.created_at).toLocaleString(),
        modified_at: new Date(data.modified_at).toLocaleString(),
      };
    },
    loadNewTask() {
      this.toggleModal("addTaskModal");
      this.toggleModal("loadTaskModal");
      let id =
        "t" + new Date().getTime().toString() + this.generateUniqueString();
      this.task.itemID = id;
      this.currentItemID = id;
      this.task.vehicle.price = this.gokarts.find(
        (o) => o.name === this.task.vehicle.name
      )?.price;
      this.task.duebal = this.task.vehicle.price;
      this.task.isPaid = false;
      this.task.isCompleted = false;
      this.task.actualStartTime = new Date().toLocaleTimeString();
      this.saveAction();
    },
    completeTask() {
      if (!this.task.isPaid) {
        return;
      }
      this.task.isCompleted = !this.task.isCompleted;
      this.task.completionDate = this.task.isCompleted
        ? new Date().toLocaleString()
        : "";
      this.saveAction();
    },
    async saveAction() {
      let data = {
        clientname: this.task.clientname,
        actualStartTime: this.task.actualStartTime,
        startDate: this.task.startDate,
        endDate: this.task.endDate,
        vehicle: this.task.vehicle.name,
        duebal: this.gokarts.find((o) => o.name === this.task.vehicle.name)
          ?.price,
        isPaid: this.task.isPaid,
        desc: this.task.desc,
        status: this.task.status.name,
        itemID: this.task.itemID,
        isCompleted: this.task.isCompleted,
        completionDate: this.task.completionDate,
        processedBy: this.userdata.fName + " " + this.userdata.lName,
      };

      await axios.get(this.API_URL + "gokart/").then(async (response) => {
        this.tasks = response.data;
        const isDataExists =
          this.tasks.findIndex((o) => o.itemID === data.itemID) !== -1;
        if (!isDataExists) {
          this.tasks.push(data);

          // Make a POST request to the API to save the data
          await axios
            .post(this.API_URL + "gokart/", data)
            .then((response) => {
              // Log a success message to the console
            })
            .catch((error) => {
              // Log an error message to the console
              console.error("Error saving data:", error);
            });
        } else {
          this.generateArrayID(this.currentItemID);
          let item = this.tasks[this.itemIndex];
          item.clientname = data.clientname;
          item.actualStartTime = data.actualStartTime;
          item.startDate = data.startDate;
          item.endDate = data.endDate;
          item.vehicle = data.vehicle;
          item.isPaid = data.isPaid;
          item.duebal = data.duebal;
          item.taskdesc = data.taskdesc;
          item.status = data.status;
          item.isCompleted = data.isCompleted;
          item.completionDate = data.completionDate;

          await axios.put(`${this.API_URL}gokart/${item.id}/`, data);
        }

        this.populateCalendarItems();
      });
    },
    updateTasks() {
      this.saveAction();
    },
    addNewTask() {
      this.task.clientname = "";
      this.task.vehicle = {
        name: "",
        price: 0,
        isEditing: false,
      };
      this.task.status = {
        name: "Booked",
        isEditing: false,
      };
      this.task.completionDate = "";
      this.task.desc = "";
      this.task.created_at = new Date().toLocaleString();
      this.task.modified_at = new Date().toLocaleString();

      this.toggleModal("addTaskModal");
    },
    async loadData() {
      const response = await axios.get(this.API_URL + "gokart/");
      this.tasks = response.data;

      const response2 = await axios.get(this.API_URL + "gokartvehicle/");
      this.gokarts = response2.data.filter((o) => {
        return o.isAvailable;
      });

      this.populateCalendarItems();
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
      let today = new Date();
      this.dayreserve = d;
      if (this.dayreserve.setHours(0, 0, 0, 0) < today.setHours(0, 0, 0, 0)) {
        return;
      }
      if (
        this.userdata.role !== "supervisor" &&
        this.userdata.role !== "superuser"
      ) {
        return;
      }
      this.dayreserve = d;
      this.task.startDate = formatDate(this.dayreserve);
      this.task.endDate = formatDate(this.dayreserve);
      this.addNewTask();
    },
    setSelection(dateRange) {
      // if (
      //   this.userdata.role !== "supervisor" &&
      //   this.userdata.role !== "superuser"
      // ) {
      //   return;
      // }
      // this.selectionEnd = dateRange[1];
      // this.selectionStart = dateRange[0];
    },
    finishSelection(dateRange) {
      // let today = new Date();
      // this.dayreserve = dateRange;
      // if (this.dayreserve.setHours(0, 0, 0, 0) < today.setHours(0, 0, 0, 0)) {
      //   return;
      // }
      // if (
      //   this.userdata.role !== "supervisor" &&
      //   this.userdata.role !== "superuser"
      // ) {
      //   return;
      // }
      // this.task.startDate = formatDate(dateRange[0]);
      // this.task.endDate = formatDate(dateRange[1]);
      // this.addNewTask();
    },
    onDrop(item, date) {
      let today = new Date();
      if (date.setHours(0, 0, 0, 0) < today.setHours(0, 0, 0, 0)) {
        return;
      }
      if (
        this.userdata.role !== "supervisor" &&
        this.userdata.role !== "superuser"
      ) {
        return;
      }
      this.setInitialData(item);
      const data = this.tasks[this.itemIndex];
      if (data.isCompleted) {
        return;
      }
      const eLength = CalendarMath.dayDiff(item.startDate, date);
      if (event.ctrlKey) {
        // let sd = CalendarMath.addDays(item.startDate, 0);
        // let ed = CalendarMath.addDays(
        //   item.endDate,
        //   eLength - CalendarMath.dayDiff(item.startDate, item.endDate)
        // );
        // if (ed >= sd) {
        //   item.originalItem.startDate = sd;
        //   item.originalItem.endDate = ed;
        //   this.task.startDate = formatDate(sd);
        //   this.task.endDate = formatDate(ed);
        // } else {
        //   item.originalItem.endDate = item.endDate;
        //   item.originalItem.startDate = ed;
        //   this.task.startDate = formatDate(ed);
        //   this.task.endDate = formatDate(item.endDate);
        // }
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
      this.task.status.name = "Booked";
      this.populateCalendarItems();
      this.saveAction();
    },
    onClickItem(e) {
      this.setInitialData(e);
      this.toggleModal("loadTaskModal");
    },
    populateCalendarItems() {
      this.calendarItems = this.tasks.map((task) => {
        const startDate = task.startDate;
        const endDate = task.endDate;
        const title = `${task.clientname}-${task.vehicle}-${task.isPaid}<span style="display:none">~${task.itemID}~</span>`;
        const id = task.itemID;
        const tooltip = "test";
        let classes = "";
        if (task.status === "Booked") {
          classes = ["task-booked"];
        } else if (task.status === "Rented") {
          classes = ["task-rented"];
        } else {
          classes = ["task-returned"];
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
    if (
      this.userdata.role !== "supervisor" &&
      this.userdata.role !== "superuser"
    ) {
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
  background-image: linear-gradient(
      rgba(255, 255, 255, 0.5),
      rgba(255, 255, 255, 0.5)
    ),
    url("@/assets/gokartbanner.jpg");
  background-repeat: "no-repeat";
  background-position: "center";
  background-size: "cover";
  background-attachment: "fixed";
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

.task-rented {
  background-color: rgb(0, 170, 255);
  /* adjust the color as needed */
}

.task-returned {
  background-color: rgb(46, 215, 216);
  /* adjust the color as needed */
}

.task-booked {
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

/*left right modal*/
.modal.left_modal,
.modal.right_modal {
  position: fixed;
  z-index: 1056;
}
.modal.left_modal .modal-dialog,
.modal.right_modal .modal-dialog {
  position: fixed;
  margin: auto;
  width: 40%;
  height: 100%;
  -webkit-transform: translate3d(0%, 0, 0);
  -ms-transform: translate3d(0%, 0, 0);
  -o-transform: translate3d(0%, 0, 0);
  transform: translate3d(0%, 0, 0);
}

.modal-dialog {
  /* max-width: 100%; */
  margin: 1.75rem auto;
}
@media (min-width: 576px) {
  .left_modal .modal-dialog {
    max-width: 100%;
  }

  .right_modal .modal-dialog {
    max-width: 100%;
  }
}
.modal.left_modal .modal-content,
.modal.right_modal .modal-content {
  /*overflow-y: auto;
    overflow-x: hidden;*/
  height: 100vh !important;
}

.modal.left_modal .modal-body,
.modal.right_modal .modal-body {
  padding: 15px 15px 30px;
}

/*.modal.left_modal  {
    pointer-events: none;
    background: transparent;
}*/

.modal-backdrop {
  display: none;
}

/*Left*/
.modal.left_modal.fade .modal-dialog {
  left: -50%;
  -webkit-transition:
    opacity 0.3s linear,
    left 0.3s ease-out;
  -moz-transition:
    opacity 0.3s linear,
    left 0.3s ease-out;
  -o-transition:
    opacity 0.3s linear,
    left 0.3s ease-out;
  transition:
    opacity 0.3s linear,
    left 0.3s ease-out;
}

.modal.left_modal.fade.show .modal-dialog {
  left: 0;
  box-shadow: 0px 0px 19px rgba(0, 0, 0, 0.5);
}

/*Right*/
.modal.right_modal.fade .modal-dialog {
  right: -50%;
  -webkit-transition:
    opacity 0.3s linear,
    right 0.3s ease-out;
  -moz-transition:
    opacity 0.3s linear,
    right 0.3s ease-out;
  -o-transition:
    opacity 0.3s linear,
    right 0.3s ease-out;
  transition:
    opacity 0.3s linear,
    right 0.3s ease-out;
}

.modal.right_modal.fade.show .modal-dialog {
  right: 0;
  box-shadow: 0px 0px 19px rgba(0, 0, 0, 0.5);
}

/* ----- MODAL STYLE ----- */
.modal-content {
  border-radius: 0;
  border: none;
}

.modal-header.left_modal,
.modal-header.right_modal {
  padding: 10px 15px;
  border-bottom-color: #eeeeee;
  background-color: #fafafa;
}

.modal_outer .modal-body {
  /*height:90%;*/
  overflow-y: auto;
  overflow-x: hidden;
  height: 91vh;
}
</style>
