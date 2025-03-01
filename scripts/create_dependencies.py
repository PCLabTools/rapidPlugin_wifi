FILEPATH_DEPENDENCY_H = project_path + '/include/wifi.h'

contents = '''/**
 * @file wifi.h
 * @author your name (you@domain.com)
 * @brief 
 * @version 0.1
 * @date 2025-02-08
 * 
 * @copyright Copyright (c) 2025
 * 
 */

// #define rapidPlugin_wifi_override_main_loop
// #define rapidPlugin_wifi_override_interface

#ifndef wifi_h
#define wifi_h

#include "errors.h"

#include "rapidPlugin_wifi.h"

#ifdef rapidPlugin_wifi_override_main_loop
/**
 * @brief main loop task
 * 
 * @param pModule pointer to the calling object
 */
void rapidPlugin_wifi::main_loop(void* pModule)
{
  rapidPlugin_wifi* plugin = (rapidPlugin_wifi*)pModule;
  for ( ;; )
  {
    // do something here
    vTaskDelay(1000 / portTICK_PERIOD_MS);
  }
}
#endif

#ifdef rapidPlugin_wifi_override_interface
/**
 * @brief Interface handler extended functions.
 * This function is to be used for creating custom states 
 * that are called when rapidFunction commands are received
 * 
 * @param incoming message broken into 2 strings: function and parameters
 * @param messageBuffer buffer to store return message
 * @return uint8_t return 0 if the function was handled, 1 if not
 */
uint8_t rapidPlugin_wifi::interface(rapidFunction incoming, char messageBuffer[])
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

#endif // wifi_h

'''

try:
  open(FILEPATH_DEPENDENCY_H, "r+")
  print(info + '\'wifi.h\' already present')
except:
  print(warning + '\'wifi.h\' not present, generating default...')
  try:
    with open(FILEPATH_DEPENDENCY_H, 'x') as f:
      f.write(contents)
  except:
    print(error + '\'wifi.h\' could not be written to')