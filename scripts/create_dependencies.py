FILEPATH_DEPENDENCY_H = project_path + '/include/template.h'

contents = '''/**
 * @file template.h
 * @author your name (you@domain.com)
 * @brief 
 * @version 0.1
 * @date 2025-02-08
 * 
 * @copyright Copyright (c) 2025
 * 
 */

// #define rapidPlugin_template_override_main_loop
// #define rapidPlugin_template_override_interface

#ifndef template_h
#define template_h

#include "errors.h"

#include "rapidPlugin_template.h"

#ifdef rapidPlugin_template_override_main_loop
/**
 * @brief main loop task
 * 
 * @param pModule pointer to the calling object
 */
void rapidPlugin_template::main_loop(void* pModule)
{
  rapidPlugin_template* plugin = (rapidPlugin_template*)pModule;
  for ( ;; )
  {
    // do something here
    vTaskDelay(1000 / portTICK_PERIOD_MS);
  }
}
#endif

#ifdef rapidPlugin_template_override_interface
/**
 * @brief Interface handler extended functions.
 * This function is to be used for creating custom states 
 * that are called when rapidFunction commands are received
 * 
 * @param incoming message broken into 2 strings: function and parameters
 * @param messageBuffer buffer to store return message
 * @return uint8_t return 0 if the function was handled, 1 if not
 */
uint8_t rapidPlugin_template::interface(rapidFunction incoming, char messageBuffer[])
{
  do
  {
    if (!strcmp(incoming.function, "random"))
    {
      int min = 0, max = 0;
      sscanf(incoming.parameters, "%d,%d", &min, &max);
      int result = rand() % (max - min) + min;
      sprintf(messageBuffer, "random_example(%d,%d) = %d", min, max, result);
      continue;
    }
    rapidPlugin::interface(incoming, messageBuffer);
    return 0;
  } while (false);
  return 1;
}
#endif

#endif // template_h

'''

try:
  open(FILEPATH_DEPENDENCY_H, "r+")
  print(info + '\'template.h\' already present')
except:
  print(warning + '\'template.h\' not present, generating default...')
  try:
    with open(FILEPATH_DEPENDENCY_H, 'x') as f:
      f.write(contents)
  except:
    print(error + '\'template.h\' could not be written to')