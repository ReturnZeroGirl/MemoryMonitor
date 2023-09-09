using System.Diagnostics;

public static void PrintMemoryUsageInMB()
{
    PerformanceCounter totalMemoryCounter = new PerformanceCounter("Memory", "Available MBytes");
    PerformanceCounter usedMemoryCounter = new PerformanceCounter("Process", "Working Set", "_Total");

    double totalMemoryInMB = totalMemoryCounter.NextValue();
    double usedMemoryInMB = usedMemoryCounter.NextValue() / (1024.0 * 1024.0);

    Console.WriteLine($"Total memory: {totalMemoryInMB} MB");
    Console.WriteLine($"Used memory: {usedMemoryInMB} MB");
}
