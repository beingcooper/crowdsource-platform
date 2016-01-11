(function () {
    'use strict';

    angular
        .module('crowdsource.project.controllers')
        .controller('MyTasksController', MyTasksController);

    MyTasksController.$inject = ['$scope', 'Project', '$routeParams', 'Task', '$mdToast',
        '$filter', 'RatingService'];

    /**
     * @namespace MyTasksController
     */
    function MyTasksController($scope, Project, $routeParams, Task, $mdToast, $filter, RatingService) {
        var self = this;
        self.projects = [];
        self.loading = true;
        self.isSelected = isSelected;
        self.selectedProject = null;
        self.toggleSelected = toggleSelected;
        self.getStatus = getStatus;
        self.listMyTasks = listMyTasks;
        self.setRating = setRating;
        self.filterByStatus = filterByStatus;
        self.tasks = [];
        self.status = {
            RETURNED: 5,
            REJECTED: 4,
            ACCEPTED: 3,
            SUBMITTED: 2,
            IN_PROGRESS: 1
        };
        activate();
        function activate() {
            Project.listWorkerProjects().then(
                function success(response) {
                    self.loading = false;
                    self.projects = response[0];
                },
                function error(response) {
                    $mdToast.showSimple('Could not get tasks.');
                }
            ).finally(function () {
            });
        }


        function isSelected(project) {
            return angular.equals(project, self.selectedProject);
        }

        function toggleSelected(item) {
            if (angular.equals(item, self.selectedProject)) {
                self.selectedProject = null;
                self.tasks = [];
            }
            else {
                self.listMyTasks(item);
            }
        }


        function getStatus(statusId) {
            for (var key in self.status) {
                if (self.status.hasOwnProperty(key)) {
                    if (statusId == self.status[key])
                        return key;
                }

            }
        }

        function listMyTasks(project) {
            Task.listMyTasks(project.id).then(
                function success(response) {
                    self.tasks = response[0].tasks;
                    self.selectedProject = project;
                    RatingService.listByTarget(project.owner.profile, 'worker').then(
                        function success(response) {
                            self.selectedProject.rating = response[0];
                        },
                        function error(response) {
                            $mdToast.showSimple('Could requester rating');
                        }
                    ).finally(function () {
                    });
                },
                function error(response) {
                    $mdToast.showSimple('Could fetch project tasks');
                }
            ).finally(function () {
            });
        }

        function setRating(rating, weight) {
            if (rating && rating.hasOwnProperty('id') && rating.id) {
                RatingService.updateRating(weight, rating).then(function success(resp) {
                    rating.weight = weight;
                }, function error(resp) {
                    $mdToast.showSimple('Could not update rating.');
                }).finally(function () {

                });
            } else {
                RatingService.submitRating(weight, rating).then(function success(resp) {
                    rating.id = resp[0].id;
                    rating.weight = weight;
                }, function error(resp) {
                    $mdToast.showSimple('Could not submit rating.')
                }).finally(function () {

                });
            }
        }
        function filterByStatus(status){
            return $filter('filter')(self.tasks, {'task_status': status})
        }
    }
})();