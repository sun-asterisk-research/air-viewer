export default {

  // home is a section without childs, set as an empty array
  home: [],

  nodes: [

    {
      type: 'title',
      txt: 'Nodes',
      icon: 'fa fa-tag context-menu__title-icon'
    },

    {
      type: 'link',
      txt: 'List Nodes',
      link: '/admin/node'
    },

    {
      type: 'link',
      txt: 'Add New Node',
      link: '/admin/node'
    }
  ]
}
