import React, { useState } from 'react';
import { Camera, RotateCw, ZoomIn, Settings, RefreshCw, Crop, Monitor, Film, Globe, PlayCircle } from 'lucide-react';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Tabs, TabsContent, TabsList, TabsTrigger } from '@/components/ui/tabs';

export default function ScoreSight() {
  const [selectedSource, setSelectedSource] = useState('select');
  const [isToolsEnabled, setIsToolsEnabled] = useState(false);
  
  return (
    <div className="flex h-screen bg-gray-100">
      {/* Left Panel */}
      <div className="w-80 bg-white border-r border-gray-200 flex flex-col">
        <div className="p-4 flex flex-col gap-4">
          {/* Box Info Section */}
          <Card>
            <CardHeader>
              <CardTitle className="text-sm">Box Information</CardTitle>
            </CardHeader>
            <CardContent>
              <div className="flex gap-2">
                <table className="w-full border-collapse">
                  <thead>
                    <tr>
                      <th className="text-left text-sm">Field</th>
                      <th className="text-left text-sm">Value</th>
                    </tr>
                  </thead>
                  <tbody>
                    {/* Table content would be dynamically populated */}
                  </tbody>
                </table>
                <div className="flex flex-col gap-1">
                  <button className="w-7 h-7 bg-gray-100 rounded flex items-center justify-center font-bold">+</button>
                  <button className="w-7 h-7 bg-gray-100 rounded flex items-center justify-center font-bold">-</button>
                </div>
              </div>
              <div className="flex gap-2 mt-2">
                <button className="flex-1 px-3 py-1 bg-blue-500 text-white rounded disabled:opacity-50">
                  Add to Scene →
                </button>
                <button className="flex-1 px-3 py-1 bg-red-500 text-white rounded disabled:opacity-50">
                  Remove Selected
                </button>
              </div>
            </CardContent>
          </Card>

          {/* Target Settings */}
          <Card>
            <CardHeader className="pb-2">
              <div className="flex justify-between items-center">
                <CardTitle className="text-sm">Target Settings</CardTitle>
                <button className="px-2 py-1 text-sm bg-gray-100 rounded">Defaults</button>
              </div>
            </CardHeader>
            <CardContent className="grid grid-cols-2 gap-2">
              <div className="flex items-center gap-2">
                <label className="text-sm">Type</label>
                <select className="flex-1 text-sm p-1 border rounded">
                  <option>Number 0-9</option>
                  <option>Time 0-9 , . :</option>
                  <option>Text</option>
                </select>
              </div>
              <div className="flex items-center gap-2">
                <label className="text-sm">Format</label>
                <select className="flex-1 text-sm p-1 border rounded">
                  <option>Time mm:ss.d</option>
                  <option>Time mm:ss</option>
                  <option>Score 1dd</option>
                </select>
              </div>
              {/* More settings as checkboxes */}
              <div className="col-span-2">
                <label className="flex items-center gap-2">
                  <input type="checkbox" />
                  <span className="text-sm">Average Output</span>
                </label>
              </div>
              <div className="col-span-2">
                <label className="flex items-center gap-2">
                  <input type="checkbox" />
                  <span className="text-sm">Skip Empty Values</span>
                </label>
              </div>
            </CardContent>
          </Card>

          {/* Output Tabs */}
          <Tabs defaultValue="text-files" className="w-full">
            <TabsList className="grid w-full grid-cols-5">
              <TabsTrigger value="text-files">Text</TabsTrigger>
              <TabsTrigger value="browser">Browser</TabsTrigger>
              <TabsTrigger value="obs">OBS</TabsTrigger>
              <TabsTrigger value="vmix">VMix</TabsTrigger>
              <TabsTrigger value="api">API</TabsTrigger>
            </TabsList>

            <TabsContent value="text-files">
              <Card>
                <CardContent className="pt-4">
                  <div className="flex flex-col gap-2">
                    <div className="flex items-center gap-2">
                      <label className="text-sm w-16">Folder</label>
                      <input type="text" className="flex-1 text-sm p-1 border rounded" readOnly />
                      <button className="px-2 py-1 text-sm bg-gray-100 rounded">Open</button>
                    </div>
                    <div className="flex gap-4">
                      <label className="flex items-center gap-2">
                        <input type="checkbox" />
                        <span className="text-sm">Save .csv file</span>
                      </label>
                      <label className="flex items-center gap-2">
                        <input type="checkbox" />
                        <span className="text-sm">Save .xml file</span>
                      </label>
                    </div>
                  </div>
                </CardContent>
              </Card>
            </TabsContent>
            
            {/* Other tab contents would be similar */}
          </Tabs>
        </div>
      </div>

      {/* Right Panel */}
      <div className="flex-1 flex flex-col">
        {/* Source Selection */}
        <div className="p-4 bg-white border-b border-gray-200">
          <div className="flex items-center gap-2">
            <span className="text-sm">Source</span>
            <select 
              className="flex-1 max-w-xs p-1 text-sm border rounded"
              value={selectedSource}
              onChange={(e) => setSelectedSource(e.target.value)}
            >
              <option value="select">Select a source</option>
              <option value="file">Open a Video File</option>
              <option value="url">URL Source (HTTP, RTSP)</option>
              <option value="screen">Screen Capture</option>
            </select>
            <button className="p-1 text-gray-600 disabled:opacity-50" disabled={!isToolsEnabled}>
              <Settings size={18} />
            </button>
            <button className="p-1 text-gray-600">
              <RefreshCw size={18} />
            </button>
          </div>

          {/* Tools */}
          <div className="flex items-center gap-2 mt-2">
            <button className="p-1 text-gray-600 hover:bg-gray-100 rounded">
              <Monitor size={18} />
            </button>
            <button className="p-1 text-gray-600 hover:bg-gray-100 rounded">
              <Crop size={18} />
            </button>
            <button className="p-1 text-gray-600 hover:bg-gray-100 rounded">
              <RotateCw size={18} />
            </button>
            <div className="flex-1" />
            <select className="text-sm p-1 border rounded">
              <option>No Box</option>
              <option>Outline</option>
              <option>Names</option>
              <option>All</option>
            </select>
            <button className="p-1 text-gray-600 hover:bg-gray-100 rounded">
              <ZoomIn size={18} />
            </button>
          </div>
        </div>

        {/* Main Content Area */}
        <div className="flex-1 bg-gray-50 flex items-center justify-center">
          {selectedSource === 'select' ? (
            <div className="text-gray-500 text-lg">
              Open a Camera or Load a File
            </div>
          ) : (
            <div className="relative w-full h-full">
              {/* Video content would go here */}
            </div>
          )}
        </div>
      </div>
    </div>
  );
}