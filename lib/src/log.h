#pragma once
#include <stdarg.h>

#ifdef __cplusplus
extern "C" {
#endif

#define MEDUSSA_LOGLEVEL_LABELS(v) \
    v(ERROR) \
    v(WARN) \
    v(INFO) \
    v(DEBUG)

typedef enum loglevel_ {
#define MEDUSSA_LOGLEVEL_ENUM(l)  l,
    MEDUSSA_LOGLEVEL_LABELS(MEDUSSA_LOGLEVEL_ENUM)
} loglevel;

void vlogf_(loglevel l, const char* source_file, unsigned source_line, const char* format, va_list args);
void logf_(loglevel l, const char* source_file, unsigned source_line, const char* format, ...);

#define logf(loglevel, ...) logf_(loglevel, __FILE__, __LINE__, __VA_ARGS__)
#define debug(...) logf(DEBUG, __VA_ARGS__)
#define info(...) logf(INFO, __VA_ARGS__)
#define warn(...) logf(WARN, __VA_ARGS__)
#define error(...) logf(ERROR, __VA_ARGS__)

#ifdef __cplusplus
}
#endif
