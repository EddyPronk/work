set APP=Foo

rem Class library
del /S /Q %APP%
mkdir %APP%
pushd %APP%
dotnet new classlib
popd

rem Application
del /S /Q %APP%.App
mkdir %APP%.App
pushd %APP%.App
dotnet new console
dotnet add reference ../%APP%/%APP%.csproj
popd

rem Tests
del /S /Q %APP%.Tests
mkdir %APP%.Tests
pushd %APP%.Tests
dotnet new mstest
dotnet add reference ../%APP%/%APP%.csproj
popd

rem Solution
del aws-task1.sln
dotnet new sln
dotnet sln add .\%APP%\%APP%.csproj
dotnet sln add .\%APP%.App\%APP%.App.csproj
dotnet sln add .\%APP%.Tests\%APP%.Tests.csproj

del /S /Q %APP%\obj
del /S /Q %APP%.App\obj
del /S /Q %APP%.Tests\obj
