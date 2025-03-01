/**
 * @file rapidPlugin_template.h
 * @author your name (you@domain.com)
 * @brief 
 * @version 0.1
 * @date 2023-10-22
 * 
 * @copyright Copyright (c) 2023
 * 
 */

#ifndef rapidPlugin_template_h
#define rapidPlugin_template_h

#ifndef rapidPlugin_template_stack_size
#define rapidPlugin_template_stack_size 64
#endif

#ifndef rapidPlugin_template_interface_stack_size
#define rapidPlugin_template_interface_stack_size 256
#endif

#include "rapidRTOS.h"

/**
 * @brief rapidPlugin top level description
 * 
 */
class rapidPlugin_template : public rapidPlugin
{
  public:
    rapidPlugin_template(const char* identity);
    BaseType_t run();
    BaseType_t runCore(BaseType_t core);

  private:
    static void main_loop(void*);
    uint8_t interface(rapidFunction incoming, char messageBuffer[]);
};

/**
 * @brief Construct a new rapidPlugin_template object
 * 
 * @param identity string literal containing task name
 */
rapidPlugin_template::rapidPlugin_template(const char* identity)
{
  _pID = identity;
}

/**
 * @brief Runs the main loop task.
 * rapidRTOS registers the task with the manager and creates the interface handlers
 * 
 * @return BaseType_t 1 = task run successful | 0 = task failed to start
 */
BaseType_t rapidPlugin_template::run()
{
  return rapidPlugin::run(&main_loop, rapidPlugin_template_stack_size, rapidPlugin_template_interface_stack_size);
}

/**
 * @brief Runs the main loop task on the specified core.
 * rapidRTOS registers the task with the manager and creates the interface handlers
 * using the same core as the main loop
 * 
 * @param core core ID
 * @return BaseType_t 1 = task run successful | 0 = task failed to start
 */
BaseType_t rapidPlugin_template::runCore(BaseType_t core)
{
  return rapidPlugin::runCore(core, &main_loop, rapidPlugin_template_stack_size, rapidPlugin_template_interface_stack_size);
}

#ifndef rapidPlugin_template_override_main_loop
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

#ifndef rapidPlugin_template_override_interface
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

#include "template.h"

#endif // rapidPlugin_template_h