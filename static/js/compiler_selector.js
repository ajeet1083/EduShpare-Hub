function select_compiler(compiler) {
  var compilerUrl;
  switch (compiler) {
      case 'java':
          compilerUrl = 'https://www.jdoodle.com/embed/v1/d5ccec05612d05f1';
          break;
      case 'python':
          compilerUrl = 'https://www.jdoodle.com/embed/v1/19e78fadb13b991a';
          break;
      case 'c':
          compilerUrl = 'https://www.jdoodle.com/embed/v1/4bdb182b6c9ae32e';
          break;
      case 'c++':
          compilerUrl = 'https://www.jdoodle.com/embed/v1/4cbb930fd6a8bd45';
          break;
      default:
          compilerUrl = 'https://www.jdoodle.com/embed/v1/19e78fadb13b991a';
  }
  
  // Create a new iframe element
  var newCompilerIframe = $('<iframe>');

  // Set the src attribute
  newCompilerIframe.attr({
    'src': compilerUrl,
    'id': 'compiler_frame',
    'width': '100%',
    'height': '450',
    'frameborder': '0',
    'marginwidth': '0',
    'marginheight': '0',
    'allowfullscreen': '',
    
});

  // Load data into newCompilerIframe
 
  // Empty #compiler_element and append the new iframe
  $("#compiler_element").empty().append(newCompilerIframe);
}
