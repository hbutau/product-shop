import Route from '@ember/routing/route';

export default class AdminCategoriesRoute extends Route {
    model() {
            // return some data we want in the template
            return [
                {
                    id: 1024, 
                    name: 'Fist Category'
                },

                {
                    id: 2048,
                    name: 'Second Category'
                }
            ];
        }

    }
