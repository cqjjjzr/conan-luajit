#include <cstring>

extern "C" {
    #include "lua.h"
    #include "lualib.h"
    #include "lauxlib.h"
}

int main(int argc, char* argv[])
{
    lua_State * L = lua_open();
    luaL_openlibs(L);
    const char* lua_script = "print('Hello World from LuaJIT!')";
    int load_stat = luaL_loadbuffer(L, lua_script, std::strlen(lua_script), lua_script);
    lua_pcall(L, 0, 0, 0);
    lua_close(L);
    return 0;
}
